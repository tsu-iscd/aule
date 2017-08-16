# Auto-generated
from aule.generated.sqlASTListener import ASTListener
from aule.generated.sqlAST import ColumnName, Star

# Types
from typing import List, Dict
from enum import Enum, IntEnum


class AccessType(Enum):
    """
    Defines accesses types, which used in pydbfw.
    This accesses types partialy maps on privileges in SQL
    """
    Select = "Select"
    Insert = "Insert"
    Update = "Update"
    Delete = "Delete"
    Replace = "Replace"
    CreateShema = "CreateShema"
    AlterSchema = "AlterSchema"
    DropSchema = "DropSchema"
    CreateTable = "CreateTable"
    AlterTable = "AlterTable"
    DropTable = "DropTable"
    CreateTablespace = "CreateTablespace"
    DropTablespace = "DropTablespace"
    CreateIndex = "CreateIndex"
    CreateProcedure = "CreateProcedure"
    CreateFunction = "CreateFunction"
    CreateView = "CreateView"
    DropView = "DropView"
    CreateTrigger = "CreateTrigger"
    CreateEvent = "CreateEvent"
    DropEvent = "DropEvent"
    CreateLogfilegroup = "CreateLogfilegroup"
    DropLogfilegroup = "DropLogfilegroup"
    CreateServer = "CreateServer"
    DropServer = "DropServer"
    Describe = "Describe"


class TableType(Enum):
    """
    Defines state of table-named-object in query.
    When we exactly knew what it is: table, alias, subquery - 
    we note this. Else it is unknown
    """
    UNKNOWN = 0
    TABLE = 1
    ALIAS = 2
    SUBQUERY = 3


class ColumnType(Enum):
    """
    Defines state of table-named-object in query.
    When we exactly knew what it is: table, alias, expression - 
    we note this. Else it is unknown.
    """
    UNKNOWN = 0
    COLUMN = 1
    ALIAS = 2
    EXPRESSION = 3
    STAR = 4


class Constants(IntEnum):
    """
    Enum consist constants used in global algorithm for
    AST traversing and access vectors collecting.
    """
    RootQueryLevel = 0
    RootQueryUID = 0


class QDescriptor:
    """
    It is used to collect full info from elementary query
    and link this query to a parent query.
    """

    def __init__(self,
                 quid,
                 tables,
                 looseColumns,
                 tablesPool,
                 columnsPool,
                 isFinished=False,
                 parentQUID=None,
                 accessType=None,
                 isPrevLevelTables=False) -> None:
        self.quid: int = quid
        self.tables: Dict = tables
        self.looseColumns: Dict = looseColumns
        self.tablesPool: Dict = tablesPool
        self.columnsPool: Dict = columnsPool
        self.isFinished: bool = isFinished
        self.parentQUID: int = parentQUID
        self.accessType: AccessType = accessType
        self.isPrevLevelTables: bool = isPrevLevelTables


class TableID:
    """
    Immutable class TableID.
    Container for full description of table in sql-statements.
    It's objects are used as identifier of tables
    """
    __slots__ = ["_table", "_schema", "_db"]

    def __init__(self, table, schema=None, db=None) -> None:
        self._table = table
        self._schema = schema
        self._db = db

    @property
    def table(self):
        return self._table

    @property
    def schema(self):
        return self._schema

    @property
    def db(self):
        return self._db

    def __str__(self) -> str:
        db = self._db if self._db else ""
        schema = "." + self._schema if self._schema else "."
        table = "." + self._table if self._table else "."
        return db + schema + table

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise ValueError()
        if key < 0 or key > 2:
            raise IndexError()
        if key == 0:
            return self._db
        if key == 1:
            return self._schema
        if key == 2:
            return self._table

    def __eq__(self, other_tid):
        if self._compare(other_tid) == 0:
            return True
        return False

    def __lt__(self, other_tid):
        if self._compare(other_tid) == -1:
            return True
        return False

    def _compare(self, other_tid):
        # Compare on each component
        i = 0
        while i < 3:
            if self[i] is None and other_tid[i] is None:
                i += 1
                continue
            if self[i] is None and other_tid[i] is not None:
                return -1
            if other_tid[i] is None:
                return 1
            if self[i] < other_tid[i]:
                return -1
            if self[i] > other_tid[i]:
                return 1
            i += 1
        return 0

    def __hash__(self):
        hash_str = ""
        hash_str += self._db if self._db else "."
        hash_str += self._schema if self._schema else "."
        hash_str += self._table if self._table else "."
        return hash(hash_str)


class ColumnID:
    """
    Class ColumnID
    Container for compound identifier of 
    column with it's state in query.
    Consist of three fields: 
      a) TableID value - identify table object in query
      b) ColumnName value - identify column object 
                             in respect of table object
                             in query
      c) ColumnType value - specify position and context 
                             of column in query
    """
    __slots__ = ["_tableId", "_columnName", "_columnType"]

    def __init__(self,
                 tableId,
                 columnName,
                 columnType=ColumnType.COLUMN) -> None:
        self._tableId = tableId
        self._columnName = columnName
        self._columnType = columnType

    @property
    def tableId(self):
        return self._tableId

    @property
    def columnName(self):
        return self._columnName

    @property
    def columnType(self):
        return self._columnType

    def __str__(self):
        tableId = "(tableId = " + str(self._tableId)
        colName = ", columnName = " + self._columnName + ", columnType=" if self._columnName else ", columnName = "
        return tableId + colName + str(self._columnType) + ")"

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise ValueError()
        if key < 0 or key > 2:
            raise IndexError()
        if key == 0:
            return self._tableId
        if key == 1:
            return self._columnName
        if key == 2:
            return self._columnType

    def __eq__(self, other_cid):
        if self._compare(other_cid) == 0 and self._columnType == other_cid.columnType:
            return True
        return False

    def __lt__(self, other_cid):
        if self._compare(other_cid) == -1:
            return True
        return False

    def _compare(self, other_cid):
        i = 0
        compareVal = (self._tableId == other_cid.tableId)
        if compareVal is False:
            if self._tableId < other_cid.tableId:
                return -1
            else:
                return 1
        if self._columnName == other_cid.columnName:
            return 0
        if self._columnName is not None:
            return 1
        if other_cid.columnName is not None:
            return -1
        if self._columnName < other_cid.columnName:
            return -1
        if self._columnName > other_cid.columnName:
            return 1
        return 0

    def __hash__(self):
        hash_str = str(self._columnType)
        hash_str += self._columnName if self._columnName else "."
        hash_str += self._tableId.table if self._tableId.table else "."
        hash_str += self._tableId.schema if self._tableId.schema else "."
        hash_str += self._tableId.db if self._tableId.db else "."
        return hash(hash_str)


class TableInfo:
    """
    class TableInfo
    It is used in order to store all collected acl-info
    for tables when walk on AST
    """

    def __init__(self, realName, tableType, accessType) -> None:
        self.realName: TableID = realName
        self.tableType: TableType = tableType
        self.accessType: AccessType = accessType


class ColumnInfo:
    """
    class ColumnInfo
    It is used in order to store all collected acl-info
    for columns when walk on AST
    """

    def __init__(self,
                 name,
                 tableKey=None,
                 realName=None,
                 columnType=None,
                 accessType=None,
                 isProcessed=False) -> None:
        self.name: str = name
        self.tableKey: TableID = tableKey
        self.realName: str = realName
        self.columnType: ColumnType = columnType
        self.accessType: str = accessType
        self.isProcessed: bool = isProcessed


class SQLAccessVectorsListener(ASTListener):
    """ This class retrieves access vectors from SQL query.
    """

    def __init__(self) -> None:
        self.accessVectors: List[Dict] = []
        self.looseAccessVectors: List[Dict] = []
        self.isBuilded: bool = False
        self.routineLevel = 0  # if we go to compound clause we increment this value
        #  if routineLevel > 0 then we NOT NEED collect acl-data
        self.routines: Dict = {}

        # base building fields
        # list of elements, each for describe separate query in Script
        self.scriptElems: List[Dict] = []
        self.curScriptElem: Dict = None
        self.curQDescriptor: QDescriptor = None

        # stacked values
        # define level or current query, 
        #  it define EXACTLY Nesting (0 for root and not nesting)
        self.currentQueryLevel = int(Constants.RootQueryLevel)
        # initialize QUID value
        self.currentQUID = int(Constants.RootQueryUID)
        # define if now (current query) we in UNION-context
        self.isUnionContext: bool = False
        self.stack_queryLevel: List[int] = []
        self.stack_QUIDs: List[int] = []
        self.stack_unionContext: List[bool] = []

        # variables defining: 
        #  current name is real name of object or alias
        self.isExactColNameContext: bool = False
        self.stack_exactColNameContext: List[bool] = []

        # next value for identifier of next query
        self.generatorQueryID = Constants.RootQueryUID + 1

    # TODO: refactor
    def merge_access_vectors(self, adding_vector) -> None:
        is_find_vector = False
        found_vector = None
        # First Find access_vectors
        for next_vector in self.accessVectors:
            if next_vector["action"] == adding_vector["action"] and next_vector["table"] == adding_vector["table"] and \
                            next_vector["schema"] == adding_vector["schema"]:
                is_find_vector = True
                found_vector = next_vector
                break
        if is_find_vector:
            for nextcolumn in adding_vector["columns"]:
                if not (nextcolumn in found_vector["columns"]):
                    found_vector["columns"].append(nextcolumn)
        else:
            self.accessVectors.append(adding_vector)

    # TODO: refactor
    def build_table_objects(self) -> None:
        nextAccessVector = None
        nextLooseAccessVector = None
        for scriptElem in self.scriptElems:
            QUIDs = list(scriptElem.keys())
            QUIDs.sort()
            # bypass all queries' descriptors
            for nextQUID in QUIDs:
                nextQDescr = scriptElem[nextQUID]
                allTablesID = list(nextQDescr.tables.keys())
                allTablesID.sort()
                looseColumns = list(nextQDescr.looseColumns.keys())
                nextResources = []
                # BUILD access_vectors
                for nextTableID in allTablesID:
                    columns = list(nextQDescr.tables[nextTableID].keys())
                    nextAccessVector = {}
                    nextAccessVector["action"] = nextQDescr.accessType.value
                    nextAccessVector["resource_type"] = "table"  # TODO: define this field dynamically
                    nextAccessVector["schema"] = nextTableID.schema
                    nextAccessVector["table"] = nextTableID.table
                    nextAccessVector["columns"] = columns
                    self.merge_access_vectors(nextAccessVector)
                    if len(looseColumns) > 0:
                        nextResources.append({"table": nextTableID.table, "schema": nextTableID.schema})
                # BUILD loose_access_vectors
                # TODO: make merge function for loose_access_vectors
                if len(looseColumns) > 0:
                    nextLooseAccessVector = {}
                    nextLooseAccessVector["action"] = nextQDescr.accessType.value
                    nextLooseAccessVector["resources"] = nextResources
                    # End special CASE
                    nextLooseAccessVector["columns"] = looseColumns
                    self.looseAccessVectors.append(nextLooseAccessVector)

    # TODO: refactor
    def build_routine_objects(self) -> None:
        routines_list = list(self.routines.keys())
        routines_list.sort()
        for routine in routines_list:
            routine_desc = self.routines[routine]
            nextAccessVector = {}
            nextAccessVector["action"] = routine_desc["action"]
            nextAccessVector["resource_type"] = routine_desc["type"]
            nextAccessVector["schema"] = routine_desc["schema"]
            nextAccessVector["routine_name"] = routine_desc["routine"]
            self.accessVectors.append(nextAccessVector)

    def build_acl(self) -> None:
        """
        Method for process accumulated QDecsriptor's vectors
         in commint ACL-vectors
        """
        if self.isBuilded:
            return
        self.build_table_objects()
        self.build_routine_objects()
        self.isBuilded = True

    def get_results(self) -> Dict:
        """
        Primary interface for return ACL-vectors from Listener 
         after it has finished job (has walked on AST).
        """
        self.build_acl()
        return {
            "access_vectors": self.accessVectors,
            "loose_access_vectors": self.looseAccessVectors
        }

    # Root-stack methods start
    def saveStack(self) -> None:
        """
        Save stack-values in stack
        """
        self.stack_queryLevel.append(self.currentQueryLevel)
        self.stack_unionContext.append(self.isUnionContext)
        self.stack_QUIDs.append(self.currentQUID)
        self.stack_exactColNameContext.append(self.isExactColNameContext)

    def restoreStack(self) -> None:
        """
        Get previous level values from stack
        """
        self.isUnionContext = self.stack_unionContext.pop()
        self.currentQUID = self.stack_QUIDs.pop()
        self.currentQueryLevel = self.stack_queryLevel.pop()
        self.isExactColNameContext = self.stack_exactColNameContext.pop()
        # restore current QDescriptor
        if self.currentQUID != Constants.RootQueryUID:
            self.curQDescriptor = self.curScriptElem[self.currentQUID]

    def statementCommonFirstActions(self, ctx) -> None:
        """
        Start process next elementary Query.
        It is necessary 
        a) save current contex information in stack,
        b) initialize new QDescriptor
        c) check if it is ending of ScriptElement and if
          it is true build full ACL-vectors in QDescriptors
          for ended ScriptElement
        """
        if self.routineLevel > 0: return

        isNextQueryLevel = False
        isNextScriptStmt = False

        # Check where we are? which context is used now? 
        #  Union? Script? or next-level statement?
        if not self.isUnionContext:
            # we NOT in union context!
            # check if we still in some exist context
            #  that mean we deep into
            #  else - we get next statement in Script
            if self.currentQUID != Constants.RootQueryUID:
                isNextQueryLevel = True
            else:
                isNextScriptStmt = True

        self.saveStack()
        # Define current statement parameters
        # level_up if necessary
        if isNextQueryLevel:
            self.currentQueryLevel += 1

        # NEXT statement from Script
        if isNextScriptStmt:
            # Initialize next scriptElement
            self.curScriptElem = {}

        # Generate next id from generator
        self.currentQUID = self.generatorQueryID
        # increment generator
        self.generatorQueryID += 1
        # Clear union_context
        self.isUnionContext = False

        # define entity-parameters for current query
        self.curScriptElem[self.currentQUID] = QDescriptor(
            quid=self.currentQUID,
            tables={},
            looseColumns={},
            tablesPool={},
            columnsPool={},
            isFinished=False,
            parentQUID=self.stack_QUIDs[len(self.stack_QUIDs) - 1],
            accessType=None
        )
        self.curQDescriptor = self.curScriptElem[self.currentQUID]

    def statementAferwordActions(self, ctx) -> None:
        """
        Finish process next elementary Query.
        Here we handle CASE when QDescriptor ending:
         process TablesPool and ColumnsPool 
         and fill QDescriptor.tables and QDescriptor.looseColumns
        """
        if self.routineLevel > 0: return
        # If this is special CASE:
        #  dependent virtual statement, hence not need Handle
        if self.curQDescriptor.isPrevLevelTables == True:
            self.restoreStack()
            return
        # 1) Preparing for analysis of Pools
        #  It is supposed that we get all info from this QDescriptor
        self.curQDescriptor.isFinished = True
        allTables = self.curQDescriptor.tablesPool
        tableIdNone = TableID(db=None, schema=None, table=None)
        columnTableId = None
        singleTableId = None
        isSingleTable = False
        cntTablesFrom = 0
        for nextTableId in allTables:
            if allTables[nextTableId].tableType != TableType.UNKNOWN:
                singleTableId = nextTableId
                cntTablesFrom += 1
                # We can handle this strange situation here
                # else:
        if cntTablesFrom == 1:
            isSingleTable = True
            singleTableId = self.curQDescriptor.tablesPool[singleTableId].realName
        # 2) Process Tables if necessary
        # 3) Process ColumnsPool
        allColumns = self.curQDescriptor.columnsPool
        for nextColumnId in self.curQDescriptor.columnsPool:
            # DEBUG START
            assert allColumns[nextColumnId].columnType is not None, "ColumnType of column not define"
            # DEBUG END

            # Process next columnId
            if allColumns[nextColumnId].isProcessed == False:
                columnTableId = None
                if allColumns[nextColumnId].columnType == ColumnType.UNKNOWN:
                    # try finding alias
                    unknownColTableKey = allColumns[nextColumnId].tableKey
                    unknownColName = allColumns[nextColumnId].name
                    findingColumnId = ColumnID(
                        tableId=unknownColTableKey,
                        columnName=unknownColName,
                        columnType=ColumnType.ALIAS
                    )
                    if findingColumnId in allColumns:
                        allColumns[nextColumnId].isProcessed = True
                        continue
                    # not alias! may be expression?
                    findingColumnId = ColumnID(
                        tableId=unknownColTableKey,
                        columnName=unknownColName,
                        columnType=ColumnType.EXPRESSION
                    )
                    if findingColumnId in allColumns:
                        allColumns[nextColumnId].isProcessed = True
                        continue
                    # not alias and not expression! It must just column!
                    allColumns[nextColumnId].columnType = ColumnType.COLUMN
                    allColumns[nextColumnId].realName = allColumns[nextColumnId].name
                # "select * ..." or "select t.* ..." - there are special CASES
                if allColumns[nextColumnId].columnType == ColumnType.STAR:
                    starRealName = allColumns[nextColumnId].realName
                    if allColumns[nextColumnId].tableKey != tableIdNone:
                        columnTableId = self.curQDescriptor.tablesPool[allColumns[nextColumnId].tableKey].realName
                        self.curQDescriptor.tables[columnTableId][starRealName] = True
                    else:
                        # * - for all tables:
                        for nextTableId in self.curQDescriptor.tables:
                            self.curQDescriptor.tables[nextTableId][starRealName] = True
                    allColumns[nextColumnId].isProcessed = True
                # BASE processing
                if allColumns[nextColumnId].columnType not in (ColumnType.EXPRESSION, ColumnType.STAR):
                    if allColumns[nextColumnId].tableKey != tableIdNone:
                        # Check if tableKey for this column present on current subquery level
                        #  if not, then this one of two: a) correlated sql-query; b) logical error sql-query
                        if allColumns[nextColumnId].tableKey in self.curQDescriptor.tablesPool:
                            columnTableId = self.curQDescriptor.tablesPool[allColumns[nextColumnId].tableKey].realName
                    if columnTableId is None and isSingleTable == True and allColumns[
                        nextColumnId].tableKey == tableIdNone:
                        columnTableId = singleTableId
                    if columnTableId is not None:
                        # ACL-access CASE
                        self.curQDescriptor.tables[columnTableId][allColumns[nextColumnId].realName] = True
                        allColumns[nextColumnId].isProcessed = True
                    else:
                        if allColumns[nextColumnId].tableKey == tableIdNone:
                            # ACL-looseAccess CASE
                            self.curQDescriptor.looseColumns[allColumns[nextColumnId].realName] = True
                            allColumns[nextColumnId].isProcessed = True
                        else:
                            # can not find table on current level
                            # MUST continue process this QDescriptor later
                            self.curQDescriptor.isFinished = False

        self.restoreStack()

        # 4) Finished ScriptElement. 
        #  Ending handle Statement in Script
        if self.currentQUID == Constants.RootQueryUID:
            # We on root-level => save current ScriptElement
            for nextQUID in self.curScriptElem:
                nextQDescr = self.curScriptElem[nextQUID]
                if nextQDescr.isFinished == False:
                    # Handle special CASE: dependent virtual statement
                    if nextQDescr.isPrevLevelTables == True:
                        # Only 1 level UP
                        for addedTableId in self.curScriptElem[nextQDescr.parentQUID].tables:
                            if addedTableId not in nextQDescr.tables:
                                nextQDescr.tables[addedTableId] = {}
                    allColumns = nextQDescr.columnsPool
                    for nextColumnId in allColumns:
                        if allColumns[nextColumnId].isProcessed == False:
                            # If can not define table => hence this is LooseAccesses
                            if allColumns[nextColumnId].tableKey == tableIdNone:
                                nextQDescr.looseColumns[allColumns[nextColumnId].name] = True
                                continue
                            foundTableID = self.findTableQUID(
                                findingTableID=allColumns[nextColumnId].tableKey,
                                parentQUID=nextQDescr.parentQUID
                            )
                            # DEBUG START
                            if foundTableID is None:
                                print(
                                    "Probably logical error in query or BUG in Collector with table = ",
                                    allColumns[nextColumnId].tableKey, " in query with UID = ", nextQUID
                                )
                                continue
                            # DEBUG END
                            nextQDescr.tables[foundTableID] = {}
                            nextQDescr.tables[foundTableID][allColumns[nextColumnId].realName] = True
                            allColumns[nextColumnId].isProcessed = True
            # Finally add current ScriptElement to common ACL list
            self.scriptElems.append(self.curScriptElem)

    def findTableQUID(self, findingTableID, parentQUID) -> TableID:
        """
        Recursive functions for finding tables
        """

        if parentQUID == Constants.RootQueryUID:
            return None

        if findingTableID in self.curScriptElem[parentQUID].tablesPool:
            # TODO: Need more analysis on TableType
            return self.curScriptElem[parentQUID].tablesPool[findingTableID].realName

        return self.findTableQUID(
            findingTableID=findingTableID,
            parentQUID=self.curScriptElem[parentQUID].parentQUID
        )

    # Bypass basic statement's node in AST start
    # DML start
    def enterUnionStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.Select
        self.isUnionContext = True

    def exitUnionStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterSelectStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.Select

    def exitSelectStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterInsertSetStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.Insert

    def exitInsertSetStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterInsertQueryStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.Insert

    def exitInsertQueryStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterInsertRowStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.Insert

    def exitInsertRowStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterUpdateSingleStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.Update

    def exitUpdateSingleStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterUpdateMultipleStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.Update

    def exitUpdateMultipleStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterDeleteSingleStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.Delete

    def exitDeleteSingleStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterDeleteMultipleStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.Delete

    def exitDeleteMultipleStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterReplaceStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.Replace

    def exitReplaceStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    # DML extend start
    def enterOnDuplicateKeyClause(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.Update
        # Fill tables for this virtual-sub-query
        self.curQDescriptor.isPrevLevelTables = True

    def exitOnDuplicateKeyClause(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    # DML extend end
    # DML end

    # DDL start
    def enterHandleDatabaseStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType(ctx.handleType + "Schema")

    def exitHandleDatabaseStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterCreateTableColumnStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.CreateTable

    def exitCreateTableColumnStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterCreateTableQueryStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.CreateTable

    def exitCreateTableQueryStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterCreateTableCopyStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.CreateTable

    def exitCreateTableCopyStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterHandleTableSpaceStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType(ctx.handleType + "Tablespace")

    def exitHandleTableSpaceStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterCreateIndexStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.CreateIndex

    def exitCreateIndexStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterCreateProcStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.CreateProcedure
        self.routineLevel += 1

    def exitCreateProcStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)
        self.routineLevel -= 1

    def enterCreateFuncStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.CreateFunction
        self.routineLevel += 1

    def exitCreateFuncStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)
        self.routineLevel -= 1

    def enterHandleViewStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType(ctx.handleType + "View")

    def exitHandleViewStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterCreateTriggerStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        routineKey = None
        schema = ctx.name.schema.name if ctx.name.schema else None
        routine = ctx.name.trigger.name
        routineKey = schema + "." if schema else "."
        routineKey += routine
        self.routines[routineKey] = {}
        self.routines[routineKey]["action"] = AccessType.CreateTrigger
        self.routines[routineKey]["schema"] = schema
        self.routines[routineKey]["routine"] = routine
        self.routines[routineKey]["type"] = "trigger"

        self.routineLevel += 1

    def exitCreateTriggerStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)
        self.routineLevel -= 1

    def enterHandleEventStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        schema = ctx.name.schema.name if ctx.name.schema else None
        routine = ctx.name.event.name
        routineKey = schema + "." if schema else "."
        routineKey += routine
        self.routines[routineKey] = {}
        self.routines[routineKey]["action"] = AccessType(ctx.handleType + "Event")
        self.routines[routineKey]["schema"] = schema
        self.routines[routineKey]["routine"] = routine
        self.routines[routineKey]["type"] = "event"
        self.routineLevel += 1

    def exitHandleEventStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)
        self.routineLevel -= 1

    def enterHandleLogFileGroupStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType(ctx.handleType + "Logfilegroup")

    def exitHandleLogFileGroupStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterHandleServerStatement(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType(ctx.handleType + "Server")

    def exitHandleServerStatement(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterBlockQueryStatement(self, ctx) -> None:
        self.routineLevel += 1

    def exitBlockQueryStatement(self, ctx) -> None:
        self.routineLevel -= 1

    # DDL end

    # Other statements start
    def enterDescribeTable(self, ctx) -> None:
        self.statementCommonFirstActions(ctx)
        self.curQDescriptor.accessType = AccessType.Describe

    def exitDescribeTable(self, ctx) -> None:
        self.statementAferwordActions(ctx)

    def enterCallStatement(self, ctx) -> None:
        if self.routineLevel > 0: return
        self.routineLevel += 1
        self.routineAdd(ctx.name, "procedure")

    def exitCallStatement(self, ctx) -> None:
        if self.routineLevel > 0: return
        self.routineLevel -= 1

    # Other statements end
    # Bypass basic statement's node in AST end

    # Bypass intermediate nodes start
    # Routines analyse start
    def routineAdd(self, ctx, routineType):
        schema = ctx.schema.name if ctx.schema else None
        routine = ctx.routine.name
        routineKey = schema + "." if schema else "."
        routineKey += routine
        if routineKey not in self.routines:
            self.routines[routineKey] = {}
            self.routines[routineKey]["action"] = "execute"
            self.routines[routineKey]["schema"] = schema
            self.routines[routineKey]["routine"] = routine
            self.routines[routineKey]["type"] = routineType

    def enterProcedureName(self, ctx) -> None:
        if self.routineLevel > 0: return
        self.routineAdd(ctx, "procedure")

    def enterUDFuncName(self, ctx) -> None:
        if self.routineLevel > 0: return
        self.routineAdd(ctx, "function")

    # Routines analyse end

    def enterWhereClause(self, ctx) -> None:
        if self.routineLevel > 0: return
        self.isExactColNameContext = True

    def exitWhereClause(self, ctx) -> None:
        if self.routineLevel > 0: return
        self.isExactColNameContext = False

    def enterFromClause(self, ctx) -> None:
        if self.routineLevel > 0: return
        self.isExactColNameContext = True

    def exitFromClause(self, ctx) -> None:
        if self.routineLevel > 0: return
        self.isExactColNameContext = False

    # Bypass intermediate nodes end

    # Bypass leaf (most important) nodes start
    def hlpAddInTablePool(self, schemaName, tableName, realTableName, aliasName, tblType):
        """
        Accumulate functionality from all Nodes where 
        it is necessary adding to TablePool
        """
        dbName = None  # while for MySQL
        tableId = None
        tableType = tblType
        if aliasName is not None:
            # CASE: ALIAS
            # CASE: SUBQUERY
            if tblType == TableType.TABLE:
                tableType = TableType.ALIAS
            tableId = TableID(db=dbName, schema=None, table=aliasName)
            self.curQDescriptor.tablesPool[tableId] = TableInfo(
                realName=TableID(db=dbName, schema=schemaName, table=realTableName),
                tableType=tableType,
                accessType=self.curQDescriptor.accessType
            )
            if schemaName is not None and tableType == TableType.ALIAS:
                tableId = TableID(db=dbName, schema=schemaName, table=aliasName)
                self.curQDescriptor.tablesPool[tableId] = TableInfo(
                    realName=TableID(db=dbName, schema=schemaName, table=realTableName),
                    tableType=tableType,
                    accessType=self.curQDescriptor.accessType
                )
        else:
            # CASE: UNKNOWN (table-obj somewhere in sql-query) - OBSOLATED
            # CASE: TABLE (table-obj in FROM without alias)
            tableId = TableID(db=dbName, schema=schemaName, table=tableName)
            self.curQDescriptor.tablesPool[tableId] = TableInfo(
                realName=TableID(db=dbName, schema=schemaName, table=realTableName),
                tableType=tableType,
                accessType=self.curQDescriptor.accessType
            )
        # Add info in Primary Table collector
        if tableType in (TableType.ALIAS, TableType.TABLE):
            if self.curQDescriptor.tablesPool[tableId].realName not in self.curQDescriptor.tables:
                self.curQDescriptor.tables[self.curQDescriptor.tablesPool[tableId].realName] = dict()

    def enterTableSource(self, ctx) -> None:
        if self.routineLevel > 0: return

        schemaName = ctx.name.schema.name if ctx.name.schema else None
        tableName = ctx.name.table.name
        aliasName = ctx.alias.name if ctx.alias else None
        self.hlpAddInTablePool(
            schemaName=schemaName, tableName=tableName,
            realTableName=tableName, aliasName=aliasName,
            tblType=TableType.TABLE
        )

    def enterSubqueryClause(self, ctx) -> None:
        if self.routineLevel > 0: return

        aliasName = ctx.alias.name
        self.hlpAddInTablePool(
            schemaName=None, tableName=None,
            realTableName=None, aliasName=aliasName,
            tblType=TableType.SUBQUERY
        )

    def enterTableName(self, ctx) -> None:
        # continue work only if current Statement is NOT SelectStatement
        if self.curQDescriptor.accessType == AccessType.Select: return
        if self.routineLevel > 0: return
        dbName = None  # while for MySQL
        schemaName = ctx.schema.name if ctx.schema else None
        tableName = ctx.table.name
        tableRealId = TableID(db=dbName, schema=schemaName, table=tableName)
        if tableRealId not in self.curQDescriptor.tablesPool:
            self.hlpAddInTablePool(
                schemaName=schemaName, tableName=tableName,
                realTableName=tableName, aliasName=None,
                tblType=TableType.TABLE
            )
        if tableRealId not in self.curQDescriptor.tables:
            self.curQDescriptor.tables[tableRealId] = {}

    def enterColumnClause(self, ctx) -> None:
        if self.routineLevel > 0: return
        self.isExactColNameContext = True
        colType = ColumnType.COLUMN
        isProcessed = False
        columnName = None
        realColumnName = None
        tableIdNone = TableID(db=None, schema=None, table=None)
        tableId = tableIdNone
        tableKeyId = tableIdNone
        aliasName = ctx.alias.name if ctx.alias else None
        # check type of columnClause
        # DEBUG
        if type(ctx.value) != ColumnName:
            colType = ColumnType.EXPRESSION
            # TODO: need more analysis
            isProcessed = True
        else:
            if type(ctx.value.column) == Star:
                realColumnName = "*"
                colType = ColumnType.STAR
            else:
                realColumnName = ctx.value.column.name
            # if we have table
            if ctx.value.table:
                schemaName = ctx.value.schema.name if ctx.value.schema else None
                tableName = ctx.value.table.name
                tableKeyId = TableID(db=None, schema=schemaName, table=tableName)
                tableId = tableKeyId
        if aliasName:
            colType = ColumnType.ALIAS
            columnName = aliasName
            # BECAUSE ALIAS CAN NOT BE WITH table
            tableId = tableIdNone
        # prepare data to add in column pool
        if colType == ColumnType.COLUMN or colType == ColumnType.STAR:
            columnName = realColumnName
        # add column in pool
        columnKey = ColumnID(
            tableId=tableId, columnName=columnName, columnType=colType
        )
        self.curQDescriptor.columnsPool[columnKey] = ColumnInfo(
            name=columnName, tableKey=tableKeyId,
            realName=realColumnName,
            columnType=colType,
            accessType=self.curQDescriptor.accessType,
            isProcessed=isProcessed
        )
        if tableKeyId != tableIdNone and realColumnName is not None:
            if tableKeyId in self.curQDescriptor.tablesPool:
                if self.curQDescriptor.tablesPool[tableKeyId].tableType in (TableType.TABLE, TableType.ALIAS):
                    self.curQDescriptor.tables[self.curQDescriptor.tablesPool[tableKeyId].realName][
                        realColumnName] = True
                    self.curQDescriptor.columnsPool[columnKey].isProcessed = True

    def exitColumnClause(self, ctx) -> None:
        if self.routineLevel > 0: return
        self.isExactColNameContext = False

    def enterColumnName(self, ctx) -> None:
        if self.routineLevel > 0: return
        # First check if there table for column
        #  and if it in TablePool
        tableIdNone = TableID(db=None, schema=None, table=None)
        tableId = tableIdNone
        # Construction type "select ... << *, t.* >> ..." can be 
        #  only in ColumnClause
        if type(ctx.column) == Star:
            return
        columnName = ctx.column.name
        colType = ColumnType.UNKNOWN
        realName = None
        if ctx.table:
            schemaName = ctx.schema.name if ctx.schema else None
            tableName = ctx.table.name
            tableId = TableID(db=None, schema=schemaName, table=tableName)
            # If there is a full name (i.e. with table name) hence
            #  it can be ONLY columnName itself, NOT alias name
            colType = ColumnType.COLUMN

        if self.isExactColNameContext == True:
            colType = ColumnType.COLUMN

        # If columnType still UNKNOWN here, then before adding this column
        #  we must check if it not erase already stored col's info
        # THIS case when 
        #   1) ColName without TableName; 
        #   2) ColName beyond Select ...; From ...; Where ...
        if colType == ColumnType.UNKNOWN:
            # Try find alias with the same fields
            testColKey = ColumnID(
                tableId=tableId, columnName=columnName,
                columnType=ColumnType.ALIAS
            )
            if testColKey in self.curQDescriptor.columnsPool:
                # Here we can CHECK if error-logical construction
                # i.e. CASE when "alias_table"."alias_column"
                # Other CASE: we have already process this column
                return
            realName = None
        else:
            realName = columnName
        columnKey = ColumnID(
            tableId=tableId, columnName=columnName,
            columnType=colType
        )
        self.curQDescriptor.columnsPool[columnKey] = ColumnInfo(
            name=columnName, tableKey=tableId, realName=realName,
            columnType=colType,
            accessType=self.curQDescriptor.accessType,
            isProcessed=False
        )
        # Not necessary code. It can be done in ExitStatement
        if tableId != tableIdNone and colType == ColumnType.COLUMN:
            if tableId in self.curQDescriptor.tablesPool:
                if self.curQDescriptor.tablesPool[tableId].tableType in (TableType.TABLE, TableType.ALIAS):
                    self.curQDescriptor.tables[self.curQDescriptor.tablesPool[tableId].realName][columnName] = True
                    self.curQDescriptor.columnsPool[columnKey].isProcessed = True
