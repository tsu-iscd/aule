from antlr4.tree.Tree import TerminalNode
from antlr4.Token import CommonToken
from aule.generated.sqlAST import *
from aule.generated.mysqlParserVisitor import mysqlParserVisitor

class mysqlASTVisitor(mysqlParserVisitor):
    """ MySQL AST Visitor. """

    def visitRoot(self, ctx):
        nodes = []
        if ctx.sql_statements():
            nodes = self.visit(ctx.sql_statements())
        iscommented = False
        # Define if SQL has comments.
        common_tokens = ctx.parser._input.tokens
        line_comment = ctx.parser.LINE_COMMENT
        comment_input = ctx.parser.COMMENT_INPUT
        for token in common_tokens:
            if token.type == line_comment or token.type == comment_input:
                iscommented = True

        return Script(bodyStatements=nodes, isCommented=iscommented)

    def visitSql_statements(self, ctx):
        sql_statements = []
        i = 0
        count = ctx.getChildCount()
        while i < count:
            child = ctx.getChild(i)
            if not isinstance(child, TerminalNode):
                if hasattr(child, "SEMI"):
                    sql_statements.append(EmptyStatement())
                else:
                    sql_statements.append(self.visit(child))
            i += 1
        return sql_statements

    # Main branches of SQL language start
    def visitEmpty_statement(self, ctx):
        return EmptyStatement()

    def visitSql_statement(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitDdl_statement(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitDml_statement(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitAdministration_statement(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitTransaction_statement(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitUtility_statement(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitReplication_statement(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitPrepared_statement(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitAnother_statement(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitCfl_compound_statement(self, ctx):
        return self.visit(ctx.getChild(0))
    # Main branches of SQL language end

    # DDL branch start
    #   DDL CREATE start
    def visitCreate_database(self, ctx):
        handletype = "create"
        ifnotexists = True if ctx.if_not_exists() else False
        dbname = SchemaName(db=None, schema=Identifier(ctx.id_().getText()))
        characterset = None
        collate = None
        isupgrade = None #TODO: make this case
        if len(ctx.create_database_option()) > 0:
            for next_create_db_opt in ctx.create_database_option():
                if next_create_db_opt.charset_name():
                    characterset = next_create_db_opt.charset_name().getText()
                if next_create_db_opt.collation_name():
                    collate = next_create_db_opt.collation_name().getText()
        return HandleDatabaseStatement(
            handleType=handletype, ifNotExist=ifnotexists, dbName=dbname, 
            charSet=characterset, collate=collate, isUpgradeDataDirectory=isupgrade
            )

    def visitCreate_event(self, ctx):
        handletype = "create"
        schema_name, event_name = self.visit(ctx.full_id())
        event = EventName(db=None, schema=schema_name, event=event_name)
        newname = None
        eventschedule = self.visit(ctx.schedule_expression())
        body = self.visit(ctx.routine_body())
        definer = self.visit(ctx.owner_statement()) if ctx.owner_statement() else None
        ifnotexists = True if ctx.if_not_exists() else False
        ispreserve = True if ctx.PRESERVE() else None
        ispreserve = False if ctx.NOT() else ispreserve
        enabletype = ctx.ENABLE().getText() if ctx.ENABLE() else None
        enabletype = ctx.DISABLE().getText() if ctx.DISABLE() else enabletype
        enabletype = "disableonslave" if ctx.SLAVE() else enabletype
        comment = ctx.STRING_LITERAL().getText() if ctx.COMMENT() else None

        return HandleEventStatement(
            handleType=handletype, name=event, newName=newname, eventSchedule=eventschedule,
            body=body, definer=definer, ifNotExist=ifnotexists, isPreserve=ispreserve,
            enableType=enabletype, comment=comment
            )

    def visitCreate_index(self, ctx):
        category = "unique" if ctx.UNIQUE() else None
        category = "fulltext" if ctx.FULLTEXT() else category
        category = "spatial" if ctx.SPATIAL() else category
        indexName = IndexName(index=Identifier(ctx.id_().getText()))
        indextype = ctx.index_type().getChild(1).getText().upper() if ctx.index_type() else None
        tableName = self.visit(ctx.table_name())
        icols = self.visit(ctx.index_colname_list())
        iopts = self.hlp_index_option_tree(ctx.index_option())
        algopt = None
        # VERY DEPEND ON GRAMMAR
        if ctx.ALGORITHM():
            algopt = ctx.getChild(ctx.getChildCount() - 1).getText()
        lockoption = None
        # VERY DEPEND ON GRAMMAR
        if ctx.LOCK():
            algopt = ctx.getChild(ctx.getChildCount() - 1).getText()
        return CreateIndexStatement(
            category=category, name=indexName, indexType=indextype, table=tableName, indexColumns=icols,
            indexOptions=iopts, algorithmOption=algopt, lockOption=lockoption
            )

    def hlp_index_option_tree(self, options_tree):
        ioptions = IndexOptionSet()
        length_options_tree = len(options_tree)
        index = 0
        while index < length_options_tree:
            ioptions.keyBlockSize = options_tree[index].filesize_literal().getText() if options_tree[index].filesize_literal() else ioptions.keyBlockSize
            ioptions.indexType = options_tree[index].index_type().getChild(1).getText().upper() if options_tree[index].index_type() else ioptions.indexType
            ioptions.parser = options_tree[index].id_().getText() if options_tree[index].id_() else ioptions.parser
            ioptions.comment = options_tree[index].STRING_LITERAL().getText()[1:-1] if options_tree[index].STRING_LITERAL() else ioptions.comment
            index += 1

        return ioptions

    def visitCreate_logfile_group(self, ctx):
        handletype = "create"
        logfilegroup = LogFileGroupName(logFileGroup=Identifier(ctx.id_(0).getText()))
        undofile = ctx.undo_file.text
        initialsize = ctx.init_size.getText() if ctx.init_size else None
        undobuffersize = ctx.undo_size.getText() if ctx.undo_size else None
        redobuffersize = ctx.redo_size.getText() if ctx.redo_size else None
        nodegroup = None
        if len(ctx.id_()) > 1:
            nodegroup = Identifier(ctx.id_(1).getText())
        iswait = True if ctx.WAIT() else None
        comment = ctx.comment.text if ctx.comment else None
        engine = ctx.engine_name().getText() if ctx.engine_name() else None
        return HandleLogFileGroupStatement(
            handleType=handletype, name=logfilegroup, undoFile=undofile,
            initialSize=initialsize, undoBufferSize=undobuffersize,
            redoBufferSize=redobuffersize, nodeGroup=nodegroup,
            isWait=iswait, comment=comment, engine=engine
            )

    def visitCreate_procedure(self, ctx):
        return self.commonRoutineDef(ctx, "procedure")

    def visitCreate_function(self, ctx):
        return self.commonRoutineDef(ctx, "function")

    def commonRoutineDef(self, ctx, routine_type):
        definer = self.visit(ctx.owner_statement()) if ctx.owner_statement() else None
        schema_name, routine_name = self.visit(ctx.full_id())
        routine = None
        params = []
        routine_param_tree = None
        returntype = None
        (comment, issqllanguage, isdeterministic, sqloperation, sqlsecurity) = (None, False, None, None, None)
        if routine_type == "procedure":
            routine = ProcedureName(db=None, schema=schema_name, routine=routine_name)
            routine_param_tree = ctx.proc_param()
        if routine_type == "function":
            routine = UDFuncName(db=None, schema=schema_name, routine=routine_name)
            routine_param_tree = ctx.func_param()
            returntype = self.visit(ctx.data_type())
        for routine_param in routine_param_tree:
            params.append(self.visit(routine_param))
        body = self.visit(ctx.routine_body())
        for rchar in ctx.routine_characteristic():
            rchar_type, rchar_content = self.visit(rchar)
            if rchar_type == "comment":
                comment = rchar_content
            elif rchar_type == "issqllanguage":
                issqllanguage = rchar_content
            elif rchar_type == "isdeterministic":
                isdeterministic = rchar_content
            elif rchar_type == "sqloperation":
                sqloperation = rchar_content
            elif rchar_type == "sqlsecurity":
                sqlsecurity = rchar_content
        routine_res = None
        if routine_type == "procedure":
            routine_res = CreateProcStatement(
            definer=definer, procedure=routine, params=params, body=body, comment=comment, 
            isSqlLanguage=issqllanguage, isDeterministic=isdeterministic, 
            sqlOperation=sqloperation, sqlSecurity=sqlsecurity
            )
        if routine_type == "function":
            routine_res = CreateFuncStatement(
            definer=definer, function=routine, params=params, body=body, returnType=returntype,
            comment=comment, isSqlLanguage=issqllanguage, isDeterministic=isdeterministic, 
            sqlOperation=sqloperation, sqlSecurity=sqlsecurity
            )

        return routine_res

    def visitCreate_server(self, ctx):
        handletype = "create"
        server = ServerName(server=Identifier(ctx.id_().getText()))
        wrapper = ctx.getChild(6).getText() # Very depend on grammar
        (host, database, user, password, socket, owner, port) = (None, None, None, None, None, None, None)
        for s_opt in ctx.server_option():
            if s_opt.HOST():
                host = s_opt.STRING_LITERAL().getText()
            if s_opt.DATABASE():
                database = s_opt.STRING_LITERAL().getText()
            if s_opt.USER():
                user = s_opt.STRING_LITERAL().getText()
            if s_opt.PASSWORD():
                password = s_opt.STRING_LITERAL().getText()
            if s_opt.SOCKET():
                socket = s_opt.STRING_LITERAL().getText()
            if s_opt.OWNER():
                owner = s_opt.STRING_LITERAL().getText()
            if s_opt.PORT():
                port = int(s_opt.decimal_literal().getText())
        return HandleServerStatement(
            handleType=handletype, name=server, wrapper=wrapper, host=host,
            database=database, user=user, password=password, socket=socket,
            owner=owner, port=port
            )

    def visitCopyCreateTable(self, ctx):
        istemporary = True if ctx.TEMPORARY() else False
        ifnotexists = True if ctx.if_not_exists() else False
        table = self.visit(ctx.table_name(0))
        tablecopy = self.visit(ctx.table_name(1))
        
        return CreateTableCopyStatement(
            isTemporary=istemporary, ifNotExist=ifnotexists, 
            table=table, tableCopy=tablecopy)

    def visitQueryCreateTable(self, ctx):
        istemporary = True if ctx.TEMPORARY() else False
        ifnotexists = True if ctx.if_not_exists() else False
        isreplace = True if ctx.REPLACE() else False
        isignore = True if ctx.IGNORE() else False
        table = self.visit(ctx.table_name())
        columns = []
        constraints = []
        if ctx.column_def_table_constraints():
            columns, constraints = self.visit(ctx.column_def_table_constraints())
        options = TableOptionSet()
        for opt in ctx.table_option():
            name, val = self.visit(opt)
            setattr(options, name, val)
        query = self.visit(ctx.select_statement())
        
        return CreateTableQueryStatement(
                isTemporary=istemporary, ifNotExist=ifnotexists, isReplace=isreplace,
                isIgnore=isignore, table=table, query=query, 
                columns=columns, constraints=constraints, optionSet=options
                )

    def visitColCreateTable(self, ctx):
        istemporary = True if ctx.TEMPORARY() else False
        ifnotexists = True if ctx.if_not_exists() else False
        table = self.visit(ctx.table_name())
        columns, constraints = self.visit(ctx.column_def_table_constraints())
        options = TableOptionSet()
        if ctx.table_option():
            for opt in ctx.table_option():
                name, val = self.visit(opt)
                setattr(options, name, val)
        
        return CreateTableColumnStatement(
                isTemporary=istemporary, ifNotExist=ifnotexists, table=table, 
                columns=columns, constraints=constraints, optionSet=options
                )

    def visitCreate_tablespace_innodb(self, ctx):
        handletype = "create"
        name = TablespaceName(tablespace=Identifier(ctx.id_().getText()))
        datafilename = ctx.datafile.text
        fileblocksize = ctx.fb_size.getText()
        engine = ctx.engine_name().getText() if ctx.engine_name() else None
        return HandleTableSpaceStatement(
            handleType=handletype, name=name, dataFileName=datafilename, 
            fileBlockSize=fileblocksize, engine=engine)

    def visitCreate_tablespace_ndb(self, ctx):
        handletype = "create"
        name = TablespaceName(tablespace=Identifier(ctx.id_(0).getText()))
        datafilename = ctx.datafile.text
        logfilegroup = Identifier(ctx.id_(1).getText())
        extentsize = ctx.extent_size.getText() if ctx.extent_size else None
        initialsize = ctx.initial_size.getText() if ctx.initial_size else None
        autoextendsize = ctx.autoextend_size.getText() if ctx.autoextend_size else None
        maxsize = ctx.max_size.getText() if ctx.max_size else None
        nodegroup = None
        if len(ctx.id_()) > 2:
            nodegroup = Identifier(ctx.id_(2).getText())
        iswait = True if ctx.WAIT() else False
        comment = ctx.comment.text if ctx.comment else None
        engine = ctx.engine_name().getText() if ctx.engine_name() else None
        return HandleTableSpaceStatement(
            handleType=handletype, name=name, dataFileName=datafilename, 
            logFileGroup=logfilegroup, extentSize=extentsize, initialSize=initialsize,
            autoSxtendSize=autoextendsize, maxSize=maxsize, nodeGroup=nodegroup,
            isWait=iswait, comment=comment, engine=engine)

    def visitCreate_trigger(self, ctx):
        definer = self.visit(ctx.owner_statement()) if ctx.owner_statement() else None
        schema_name, trigger_name = self.visit(ctx.this_trigger)
        trigger = TriggerName(db=None, schema=schema_name, trigger=trigger_name)
        time = ctx.trigger_time.text
        event = ctx.trigger_event.text
        tableName = self.visit(ctx.table_name())
        body = self.visit(ctx.routine_body())
        trigger_order_type = "FOLLOWS" if ctx.FOLLOWS() else None
        trigger_order_type = "PRECEDES" if ctx.PRECEDES() else trigger_order_type
        triggerorder = None
        if trigger_order_type:
            schema_name, trigger_name = self.visit(ctx.other_trigger)
            other_trigger = TriggerName(db=None, schema=schema_name, trigger=trigger_name)
            triggerorder = TriggerOrderClause(orderType=trigger_order_type, trigger=other_trigger)
        
        return CreateTriggerStatement(
            name=trigger, table=tableName, time=time, event=event, body=body,
            definer=definer, triggerOrder=triggerorder
            )

    def visitCreate_view(self, ctx):
        handletype = "create"
        algorithm = ctx.alg_type.text if ctx.alg_type else None
        definer = self.visit(ctx.owner_statement()) if ctx.owner_statement() else None
        sqlsecurity = ctx.sec_context.text if ctx.sec_context else None
        schema_name, view_name = self.visit(ctx.full_id())
        view = ViewName(db=None, schema=schema_name, view=view_name)
        cols = self.visit(ctx.id_list()) if ctx.id_list() else []
        select_stmt = self.visit(ctx.select_statement())
        opt = ctx.check_option.text if ctx.check_option else None

        return HandleViewStatement(
            handleType=handletype, name=view, columns=cols, select=select_stmt,
            algorithm=algorithm, definer=definer, sqlSecurity=sqlsecurity, checkOption=opt
            )

    #       DDL CREATE help start
    def visitCreate_database_option(self, ctx):
        pass

    def visitOwner_statement(self, ctx):
        if ctx.CURRENT_USER():
            return FixedUserName(value="currentuser")
        return self.visit(ctx.user_name())

    def visitPreciseSchedule(self, ctx):
        timestamp = self.visit(ctx.timestamp_value())
        intervals = self.hlpInterval_expr(ctx.interval_expr())
        return EventSchedulePresice(timestamp=timestamp, intervals=intervals)

    def hlpInterval_expr(self, interval_expr_list):
        intervals = []
        if interval_expr_list:
            for interval in interval_expr_list:
                intervals.append(self.visit(interval))
        return intervals

    def visitIntervalSchedule(self, ctx):
        repeatinterval = IntervalClause(
            value=int(ctx.decimal_literal().getText()), valueType=ctx.interval_type().getText())
        start = self.visit(ctx.startts) if ctx.startts else None
        startintervals = self.hlpInterval_expr(ctx.start_intervals)
        stop = self.visit(ctx.endts) if ctx.endts else None
        stopintervals = self.hlpInterval_expr(ctx.end_intervals)
        return EventScheduleInterval(
            repeatInterval=repeatinterval, start=start, startIntervals=startintervals,
            stop=stop, stopIntervals=stopintervals
            )

    def visitTimestamp_value(self, ctx):
        if ctx.CURRENT_TIMESTAMP():
            return KeywordPrimitive(keyword="CURRENT_TIMESTAMP")
        if ctx.expression():
            return self.visit(ctx.expression())
        if ctx.string_literal():
            return StringLiteral(value=ctx.getText())
        if ctx.decimal_literal():
            return NumberLiteral(value=ctx.getText())
        return None

    def visitInterval_expr(self, ctx):
        # interval_value_position = 2
        value = self.visit(ctx.getChild(2)) 
        valuetype = ctx.interval_type().getText()
        return IntervalClause(value=value, valueType=valuetype)

    def visitInterval_type(self, ctx):
        pass

    def visitIndex_type(self, ctx):
        pass

    def visitIndex_option(self, ctx):
        pass

    def visitProc_param(self, ctx):
        param_direction = ctx.getChild(0).getText().upper()
        name = Identifier(ctx.id_().getText())
        datatype = self.visit(ctx.data_type())
        return RoutineParameter(direction=param_direction, name=name, dataType=datatype)

    def visitFunc_param(self, ctx):
        name = Identifier(ctx.id_().getText())
        datatype = self.visit(ctx.data_type())
        return RoutineParameter(direction=None, name=name, dataType=datatype)

    def visitRcComment(self, ctx):
        return "comment", ctx.STRING_LITERAL().getText()

    def visitRcSqllang(self, ctx):
        return "issqllanguage", True

    def visitRcDeterm(self, ctx):
        isdeterm = False if ctx.NOT() else True
        return "isdeterministic",

    def visitRcSqldata(self, ctx):
        return "sqloperation", ctx.getText().upper()

    def visitRcSecurestmt(self, ctx):
        return "sqlsecurity", ctx.sec_context.text

    def visitServer_option(self, ctx):
        pass

    def visitColumn_def_table_constraints(self, ctx):
        """ return tuple  of list ([ColumnDefClause], [ConstraintDefClause])
        """
        columns, constraints = ([], [])
        for next_col_def_constr in ctx.column_def_table_constraint():
            columnDef, constraintDef = self.visit(next_col_def_constr)
            if columnDef is not None:
                columns.append(columnDef)
            if constraintDef is not None:
                constraints.append(constraintDef)

        return columns, constraints

    def visitColumnDefinition(self, ctx):
        # return values in format COLUMN_DEF, CONSTR_DEF
        name = Identifier(ctx.id_().getText())
        (datatype, defaultvalue, isnotnull, isautoincrement, isunique, isprimary, comment, columnformat, storage, refdef) = self.visit(ctx.column_definition())
        return ColumnDefClause(
            name=name, dataType=datatype, defaultValue=defaultvalue, 
            isNotNull=isnotnull, isAutoIncrement=isautoincrement,
            isUnique=isunique, isPrimary=isprimary, 
            comment=comment, columnFormat=columnformat, 
            storage=storage, refDef=refdef
            ), None

    def visitConstraintDefinition(self, ctx):
        # return values in format COLUMN_DEF, CONSTR_DEF
        return None, self.visit(ctx.table_constraint())

    def visitIndexDefinition(self, ctx):
        # return values in format COLUMN_DEF, CONSTR_DEF
        return None, self.visit(ctx.index_column_definition())

    def visitColumn_definition(self, ctx):
        datatype = self.visit(ctx.data_type())
        all_constr = {
            "defaultvalue":None,
            "isnotnull":False,
            "isautoincrement":False,
            "isunique":False,
            "isprimary":False,
            "comment":None,
            "columnformat":None,
            "storage":None,
            "refdef":None
        }
        for cur_constr in ctx.separate_column_constraint():
            (constr_name, constr_value) = self.visit(cur_constr)
            if constr_name == "comment":
                constr_value = constr_value[1:-1]
            all_constr[constr_name] = constr_value

        return (
            datatype, 
            all_constr["defaultvalue"], 
            all_constr["isnotnull"], 
            all_constr["isautoincrement"], 
            all_constr["isunique"], 
            all_constr["isprimary"], 
            all_constr["comment"], 
            all_constr["columnformat"], 
            all_constr["storage"], 
            all_constr["refdef"]
        )

    def visitColConstrNull(self, ctx):
        if ctx.null_notnull().NOT():
            return "isnotnull", True
        return "isnotnull", False

    def visitColConstrDflt(self, ctx):
        return "defaultvalue", self.visit(ctx.default_value())

    def visitColConstrAuInc(self, ctx):
        return "isautoincrement", True

    def visitColConstrPK(self, ctx):
        return "isprimary", True

    def visitColConstrUK(self, ctx):
        return "isunique", True

    def visitColConstrComment(self, ctx):
        return "comment", ctx.STRING_LITERAL().getText()

    def visitColConstrForm(self, ctx):
        return "columnformat", ctx.colformat.text.upper()

    def visitColConstrStorage(self, ctx):
        return "storage", ctx.storageval.text.upper()

    def visitColConstrRefdef(self, ctx):
        return "refdef", self.visit(ctx.reference_definition())

    def visitTblConstrPK(self, ctx):
        name = Identifier(ctx.constr_name.getText()) if ctx.constr_name else None
        itype = ctx.index_type().getChild(1).getText().upper() if ctx.index_type() else None
        icolumns = self.visit(ctx.index_colname_list())
        iopts = self.hlp_index_option_tree(ctx.index_option())
        return ConstraintKeyClause(
            name=name, keyType="PRIMARY", indexColumns=icolumns, 
            indexName=None, indexType=itype, indexOptionSet=iopts, refDef=None
        )

    def visitTblConstrUK(self, ctx):
        name = Identifier(ctx.constr_name.getText()) if ctx.constr_name else None
        itype = ctx.index_type().getChild(1).getText().upper() if ctx.index_type() else None
        iname = Identifier(ctx.index_name.getText()) if ctx.index_name else None
        icolumns = self.visit(ctx.index_colname_list())
        iopts = self.hlp_index_option_tree(ctx.index_option())
        return ConstraintKeyClause(
            name=name, keyType="UNIQUE", indexColumns=icolumns, 
            indexName=iname, indexType=itype, indexOptionSet=iopts, refDef=None
        )

    def visitTblConstrFK(self, ctx):
        name = Identifier(ctx.constr_name.getText()) if ctx.constr_name else None
        iname = Identifier(ctx.index_name.getText()) if ctx.index_name else None
        icolumns = self.visit(ctx.index_colname_list())
        refdef = self.visit(ctx.reference_definition()) if ctx.reference_definition() else None
        return ConstraintKeyClause(
            name=name, keyType="FOREIGN", indexColumns=icolumns, 
            indexName=iname, indexType=None, indexOptionSet=None, refDef=refdef
        )

    def visitTblConstCheck(self, ctx):
        return ConstraintCheckClause(expression=self.visit(ctx.expression()))

    def visitReference_definition(self, ctx):
        table = self.visit(ctx.table_name())
        icolumns = self.visit(ctx.index_colname_list())
        matchtype = ctx.ref_match_type.text.upper() if ctx.ref_match_type else None
        (ondelete, onupdate) = (None, None)
        if ctx.on_delete_action():
            (ondelete, onupdate) = self.visit(ctx.on_delete_action())
        if ctx.on_update_action():
            (ondelete, onupdate) = self.visit(ctx.on_update_action())
        return ReferenceDefClause(
            table=table, indexColumns=icolumns, 
            matchType=matchtype, 
            onDelete=ondelete, onUpdate=onupdate
        )

    def visitOn_delete_action(self, ctx):
        ondeleteaction = ctx.reference_action_control_type(0).getText().upper()
        onupdateaction = None
        if ctx.UPDATE():
            onupdateaction = ctx.reference_action_control_type(1).getText().upper()
        return (ondeleteaction, onupdateaction)

    def visitOn_update_action(self, ctx):
        onupdateaction = ctx.reference_action_control_type(0).getText().upper()
        ondeleteaction = None
        if ctx.DELETE():
            ondeleteaction = ctx.reference_action_control_type(1).getText().upper()
        return (ondeleteaction, onupdateaction)

    def visitReference_action_control_type(self, ctx):
        pass

    def visitSimpleIndex(self, ctx):
        itype = ctx.index_type().getChild(1).getText().upper() if ctx.index_type() else None
        iname = Identifier(ctx.id_().getText()) if ctx.id_() else None
        icolumns = self.visit(ctx.index_colname_list())
        iopts = self.hlp_index_option_tree(ctx.index_option())
        return ConstraintKeyClause(
            name=None, keyType="INDEX", indexColumns=icolumns, indexName=iname, 
            indexType=itype, indexOptionSet=iopts, refDef=None
        )

    def visitSpecIndex(self, ctx):
        keytype = ctx.getChild(0).getText().upper()
        iname = Identifier(ctx.id_().getText()) if ctx.id_() else None
        icolumns = self.visit(ctx.index_colname_list())
        iopts = self.hlp_index_option_tree(ctx.index_option())
        return ConstraintKeyClause(
            name=None, keyType=keytype, indexColumns=icolumns, indexName=iname,
            indexType=None, indexOptionSet=iopts, refDef=None
        )

    def visitTblOptEngine(self, ctx):
        return "engine", ctx.engine_name().getText().upper()

    def visitTblOptAuInc(self, ctx):
        pass #TODO

    def visitTblOptAvgRLen(self, ctx):
        pass #TODO

    def visitTblOptDefCharSet(self, ctx):
        pass #TODO

    def visitTblOptChkSum(self, ctx):
        pass #TODO

    def visitTblOptDefCollate(self, ctx):
        pass #TODO

    def visitTblOptComment(self, ctx):
        pass #TODO

    def visitTblOptCompr(self, ctx):
        pass #TODO

    def visitTblOptConn(self, ctx):
        pass #TODO
        
    def visitTblOptDataDir(self, ctx):
        pass #TODO

    def visitTblOptDelKW(self, ctx):
        pass #TODO

    def visitTblOptEncr(self, ctx):
        pass #TODO

    def visitTblOptIndexDir(self, ctx):
        pass #TODO

    def visitTblOptInsMeth(self, ctx):
        pass #TODO

    def visitTblOptKeyBlockSz(self, ctx):
        pass #TODO

    def visitTblOptMaxRows(self, ctx):
        pass #TODO

    def visitTblOptMinRows(self, ctx):
        pass #TODO

    def visitTblOptPackK(self, ctx):
        pass #TODO
        
    def visitTblOptpasswd(self, ctx):
        pass #TODO

    def visitPartition_options(self, ctx):
        pass #TODO

    def visitPartition_function_definition(self, ctx):
        pass #TODO

    def visitLinear_partition_func_def(self, ctx):
        pass #TODO

    def visitPartition_def(self, ctx):
        pass #TODO

    def visitSubpartition_def(self, ctx):
        pass #TODO


    #       DDL CREATE help end
    #   DDL CREATE end


    #   DDL ALTER start
    def visitAlter_database(self, ctx):
        pass #TODO

    def visitAlter_event(self, ctx):
        pass #TODO

    def visitAlter_function(self, ctx):
        pass #TODO
        
    def visitAlter_instance(self, ctx):
        pass #TODO
        
    def visitAlter_logfile_group(self, ctx):
        pass #TODO
        
    def visitAlter_procedure(self, ctx):
        pass #TODO
        
    def visitAlter_server(self, ctx):
        pass #TODO
        
    def visitAlter_table(self, ctx):
        pass #TODO
        
    def visitAlter_tablespace(self, ctx):
        pass #TODO
        
    def visitAlter_view(self, ctx):
        pass #TODO
    #       DDL ALTER help start
    #       DDL ALTER help end
    #   DDL ALTER end

    #   DDL DROP start
    def visitDrop_database(self, ctx):
        pass #TODO
        
    def visitDrop_event(self, ctx):
        pass #TODO
        
    def visitDrop_index(self, ctx):
        pass #TODO
        
    def visitDrop_logfile_group(self, ctx):
        pass #TODO
        
    def visitDrop_procedure(self, ctx):
        pass #TODO
        
    def visitDrop_function(self, ctx):
        pass #TODO
        
    def visitDrop_server(self, ctx):
        pass #TODO
        
    def visitDrop_table(self, ctx):
        pass #TODO
        
    def visitDrop_tablespace(self, ctx):
        pass #TODO
        
    def visitDrop_trigger(self, ctx):
        pass #TODO
        
    def visitDrop_view(self, ctx):
        pass #TODO


    #       DDL DROP help start
    #       DDL DROP help end
    #   DDL DROP end

    #   DDL Other start
    def visitRename_table(self, ctx):
        pass #TODO

    def visitTruncate_table(self, ctx):
        pass #TODO
    #   DDL Other end
    # DDL branch end

    # DML branch start
    #   DML Primary statements start
    def visitCall_statement(self, ctx):
        schema_name, routine_name = self.visit(ctx.full_id())
        procname = ProcedureName(db=None, schema=schema_name, routine=routine_name)
        expr_params = self.visit(ctx.constant_list()) if ctx.constant_list() else []
        if ctx.expression_list():
            expr_params = self.visit(ctx.expression_list())

        return CallStatement(name=procname, parameters=expr_params)

    def visitDelete_statement(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitDo_statement(self, ctx):
        pass #TODO

    def visitHandler_statement(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitInsert_statement(self, ctx):
        statementType = None if ctx.insert_statement_value() else "set"
        if statementType is None:
            statementType = "query" if ctx.insert_statement_value().select_statement() else "row"

        # VERY depend on grammar
        priority_position = 1
        if ctx.LOW_PRIORITY() or ctx.DELAYED() or ctx.HIGH_PRIORITY():
            priority = ctx.getChild(priority_position).getText()  
        else: 
            priority = None
        isignore = True if ctx.IGNORE() else False
        table = self.visit(ctx.table_name())
        column_list_num = 1 if ctx.PARTITION() else 0
        columns_id = self.visit(ctx.id_list(column_list_num)) if ctx.id_list(column_list_num) else []
        columns = []
        for cur_col_id in columns_id:
            columns.append(ColumnName(db=None, schema=None, table=None, column=cur_col_id))
        rows = []
        onduplicatekey = None
        
        # On Duplicate clause:
        if ctx.duplicate_firstelem:
            onduplicatekey = OnDuplicateKeyClause(columns=[], values=[])
            (onduplicatekey.columns, onduplicatekey.values) = self.updateElemProcess(ctx.duplicate_elem)
            onduplicatekey.columns.insert(0, self.visit(ctx.duplicate_firstelem.full_column_name()))
            onduplicatekey.values.insert(0, self.visit(ctx.duplicate_firstelem.expression()))

        if statementType == "set":
            (columns, rows) = self.updateElemProcess(ctx.set_elem)
            columns.insert(0, self.visit(ctx.set_firstelem.full_column_name()))
            rows.insert(0, self.visit(ctx.set_firstelem.expression()))
            return InsertSetStatement(
                priority=priority, isIgnore=isignore, table=table, 
                columns=columns, expressions=rows, onDuplicateKey=onduplicatekey)

        if statementType == "query":
            rows = self.visit(ctx.insert_statement_value().select_statement())
            return InsertQueryStatement(
                priority=priority, isIgnore=isignore, table=table, columns=columns, 
                query=rows, onDuplicateKey=onduplicatekey)

        # We here if only we have rows insert definiton
        rows_tree = ctx.insert_statement_value().expression_list()
        len_rows_tree = len(rows_tree)
        index = 0
        while index < len_rows_tree:
            rows.append( InsertRowClause(values=self.visit(rows_tree[index])) )
            index += 1
        return InsertRowStatement(
            priority=priority, isIgnore=isignore, table=table, 
            columns=columns, rows=rows, onDuplicateKey=onduplicatekey)

    def updateElemProcess(self, update_elems):
        (columns, values) = ([], [])
        if update_elems is None:
            return columns, values
        cnt_update_elems = len(update_elems)
        index = 0
        while index < cnt_update_elems:
            next_update_elem = update_elems[index]
            columns.append(self.visit(next_update_elem.full_column_name()))
            values.append(self.visit(next_update_elem.expression()))
            index += 1
        return columns, values

    def visitLoad_data_statement(self, ctx):
        priority = ctx.priority.text if ctx.priority else None
        replaceignore = ctx.replaceignore.text if ctx.replaceignore else None
        islocal = True if ctx.LOCAL() else False
        outfileoptions = self.formExportTextFileOptions(ctx)
        table = self.visit(ctx.table_name())
        ignorelines = int(ctx.decimal_literal().getText()) if ctx.decimal_literal() else None
        loadcolumns = []
        for next_col_or_var in ctx.col_or_uservar():
            loadcolumns.append(self.visit(next_col_or_var))
        (setcolumns, setvalues) = self.updateElemProcess(ctx.update_elem())

        return LoadDataStatement(
            priority=priority, replaceIgnore=replaceignore, isLocal=islocal,
            outFileOptionSet=outfileoptions, table=table, ignoreLines=ignorelines,
            loadColumns=loadcolumns, setColumns=setcolumns, setValues=setvalues
            )

    def formExportTextFileOptions(self, ctx):
        """ This special function for process ExportTextOptions for all command ("Load data infile" and "Select into outfile")
        """
        # VERY DEPEND on grammar
        filename = ctx.filename.text[1:-1]
        charset = ctx.charset.getText() if ctx.charset else None
        fieldsterminated = ctx.terminatefieldsymb.text[1:-1] if ctx.terminatefieldsymb else None
        fieldsenclosed = ctx.enclosedsymb.text[1:-1] if ctx.enclosedsymb else None
        fieldescaped = ctx.escapesymb.text[1:-1] if ctx.escapesymb else None
        linesstarting = ctx.startingsymb.text[1:-1] if ctx.startingsymb else None
        linesterminated = ctx.terminatelinesymb.text[1:-1] if ctx.terminatelinesymb else None

        return ExportTextFile(
            fileName=filename, charSet=charset, fieldsTerminated=fieldsterminated, 
            fieldsEnclosed=fieldsenclosed, fieldEscaped=fieldescaped, 
            linesStarting=linesstarting, linesTerminated=linesterminated
            )

    def visitLoad_xml_statement(self, ctx):
        pass #TODO

    def visitReplace_statement(self, ctx):
        pass #TODO

    def visitSimpleSelect(self, ctx):
        return self.visit(ctx.query_specification())

    def visitParenSelect(self, ctx):
        return self.visit(ctx.query_expression());

    def visitUnionSelect(self, ctx):
        (orderby, row_count, offset, clauses) = (None, None, None, [])
        clause = self.visit(ctx.query_specification_nointo())
        clauses.append(UnionClause(statement=clause))
        for cur_union_stmt in ctx.union_statement():
            clause = self.visit(cur_union_stmt)
            clauses.append(clause)

        #Check if we have last query_expression (it can be with into)
        if ctx.UNION():
            type_ = ctx.ALL().getText() if ctx.ALL() else None
            type_ = ctx.DISTINCT().getText() if ctx.DISTINCT() else type_
            if ctx.query_expression():
                clause = self.visit(ctx.query_expression())

            if ctx.query_specification():
                clause = self.visit(ctx.query_specification())
            clauses.append(UnionClause(statement=clause, unionType=type_))

        if ctx.order_by_clause():
            orderby = self.visit(ctx.order_by_clause())
        if ctx.limit_clause():
            row_count, offset = self.visit(ctx.limit_clause())
        
        return UnionStatement(
            clauses=clauses, orderByElems=orderby, 
            limitLines=row_count, limitOffset=offset)

    def visitUnionParenSelect(self, ctx):
        (orderby, row_count, offset, clauses) = (None, None, None, [])
        clause = self.visit(ctx.query_expression_nointo())
        clauses.append(UnionClause(statement=clause))
        for cur_union_stmt in ctx.union_parenth():
            clause = self.visit(cur_union_stmt)
            clauses.append(clause)

        if ctx.UNION():
            type_ = ctx.ALL().getText() if ctx.ALL() else None
            type_ = ctx.DISTINCT().getText() if ctx.DISTINCT() else type_
            clause = self.visit(ctx.query_expression())
            clauses.append(UnionClause(statement=clause, unionType=type_))

        if ctx.order_by_clause():
            orderby = self.visit(ctx.order_by_clause())
        if ctx.limit_clause():
            row_count, offset = self.visit(ctx.limit_clause())

        return UnionStatement(
            clauses=clauses, orderByElems=orderby, 
            limitLines=row_count, limitOffset=offset)

    def visitUpdate_statement(self, ctx):
        return self.visit(ctx.getChild(0))
    
    #       DML Primary statements help start
    def visitInsert_statement_value(self, ctx):
        pass

    def visitUpdate_elem(self, ctx):
        pass

    def visitCol_or_uservar(self, ctx):
        if ctx.id_():
            return ColumnName(db=None, schema=None, table=None, column=Identifier(name=ctx.id_().getText()))
        return Variable(issystem=False, name=ctx.LOCAL_ID().getText()[1:], value=None)

    #       DML Primary statements help end
    #   DML Primary statements end
    
    #   DML Detailed statements start
    def visitSingle_delete_statement(self, ctx):
        priority_position = 1
        priority = ctx.getChild(priority_position).getText() if ctx.LOW_PRIORITY() else None
        isquick = True if ctx.QUICK() else False
        isignore = True if ctx.IGNORE() else False
        table = self.visit(ctx.table_name())
        where_clauses = WhereClause(value=self.visit(ctx.expression())) if ctx.expression() else None
        orderby = self.visit(ctx.order_by_clause()) if ctx.order_by_clause() else None
        limit = int(ctx.decimal_literal().getText()) if ctx.decimal_literal() else None

        return DeleteSingleStatement(
            priority=priority, isIgnore=isignore, isQuick=isquick, 
            table=table, where=where_clauses, orderByElems=orderby, limit=limit
            )

    def visitMultiple_delete_statement(self, ctx):
        priority_position = 1
        priority = ctx.getChild(priority_position).getText() if ctx.LOW_PRIORITY() else None
        isquick = True if ctx.QUICK() else False
        isignore = True if ctx.IGNORE() else False
        if ctx.USING():
            format_ = "USING"
        else:
            format_ = "FROM"
        where_clauses = WhereClause(value=self.visit(ctx.expression())) if ctx.expression() else None
        sources = self.visit(ctx.table_sources())
        tables = []
        for cur_tbl in ctx.table_name():
            tables.append(self.visit(cur_tbl))
        
        return DeleteMultipleStatement(
            priority=priority, format_=format_, isIgnore=isignore, 
            isQuick=isquick, tables=tables, tableRefs=sources, 
            where=where_clauses)

    def visitHandler_open_statement(self, ctx):
        pass #TODO

    def visitHandler_read_index_statement(self, ctx):
        pass #TODO

    def visitHandler_read_statement(self, ctx):
        pass #TODO

    def visitHandler_close_statement(self, ctx):
        pass #TODO

    def visitSingle_update_statement(self, ctx):
        # VERY depend on grammar
        priority = ctx.LOW_PRIORITY().getText().lower() if ctx.LOW_PRIORITY() else None
        isignore = True if ctx.IGNORE() else False
        (columns, values) = self.updateElemProcess(ctx.update_elem())
        tablename = self.visit(ctx.table_name())
        tablealias = Identifier(name=ctx.id_().getText()) if ctx.id_() else None
        table = TableSource(name=tablename, alias=tablealias)
        where_expr = WhereClause(value=self.visit(ctx.expression())) if ctx.expression() else None
        orderby = self.visit(ctx.order_by_clause()) if ctx.order_by_clause() else None
        (limit, offset) = self.visit(ctx.limit_clause()) if ctx.limit_clause() else (None, None)

        return UpdateSingleStatement(
            priority=priority, isIgnore=isignore, columns=columns, 
            values=values, source=table, where=where_expr, 
            orderByElems=orderby, limit=limit)

    def visitMultiple_update_statement(self, ctx):
        priority = ctx.LOW_PRIORITY().getText().lower() if ctx.LOW_PRIORITY() else None
        isignore = True if ctx.IGNORE() else False
        (columns, values) = self.updateElemProcess(ctx.update_elem())
        sources = self.visit(ctx.table_sources())
        where_expr = WhereClause(value=self.visit(ctx.expression())) if ctx.expression() else None

        return UpdateMultipleStatement(
            priority=priority, isIgnore=isignore, columns=columns, 
            values=values, tableRefs=sources, where=where_expr)

    #       DML Detailed statements help start
    def visitOrder_by_clause(self, ctx):
        clauses = []
        index = 0
        elems = ctx.order_by_expression()
        len_elems = len(elems)
        while index < len_elems:
            clauses.append(self.visit(elems[index]))
            index += 1
        return clauses

    def visitOrder_by_expression(self, ctx):
        expr = self.visit(ctx.expression())
        sort_type = ctx.getChild(1).getText().lower() if ctx.ASC() or ctx.DESC() else None
        return SortItem(expression=expr, sortType=sort_type)

    def visitTable_sources(self, ctx):
        tables = []
        index = 0
        tbl_count = len(ctx.table_source())
        while(index < tbl_count):
            table = self.visit(ctx.table_source(index))
            tables.append(table)
            index += 1
        return tables

    def visitTable_source(self, ctx):
        tbl_source = None
        join_part_tree = ctx.join_part()
        len_join_part_tree = None
        left = None
        right = None
        jointype = None
        isnatural = None
        joincondition = None
        columnsconditions = []
        new_tbl_source = None
        # Check left FIRST argument. If it alone element or list?
        tbl_source = self.visit(ctx.table_source_item())

        # Here we have at least ONE JOIN
        if join_part_tree:
            # 0. Init step
            len_join_part_tree = len(join_part_tree)
            index = 0
            # for first iteration of while
            if isinstance(tbl_source, list):
                new_tbl_source = tbl_source
            else:
                new_tbl_source = [tbl_source]
            # Iterate all JOINs
            while index < len_join_part_tree:
                left = new_tbl_source
                right, jointype, isnatural, joincondition, columnsconditions = self.visit(join_part_tree[index])
                new_tbl_source = JoinClause(
                joinType=jointype, isNatural=isnatural, leftClauses=left, rightClauses=right, 
                joinCondition=joincondition, joinColumns=columnsconditions
                )
                index += 1

            tbl_source = new_tbl_source
        # If we have no join_part hence we have ONLY tbl_source
        #  and it is already defined
            
        return tbl_source

    def visitAtomTableItem(self, ctx):
        # Only alone table case.
        partitions = None
        alias = None
        indexhint = None #TODO: realize indexhint
        table = self.visit(ctx.table_name())
        if ctx.alias:
            alias = Identifier(ctx.alias.getText())
        if ctx.PARTITION():
            partitions = []
            terminate_partition_expression = ")"
            is_partition = False
            child_count = ctx.getChildCount()
            index = 0
            while index < child_count:
                nextchild = ctx.getChild(index)
                # Check if we have partition in table_source_item.
                if isinstance(nextchild, TerminalNode):
                    if nextchild.getText().lower() == "partition":
                        is_partition = True
                    if is_partition == True and nextchild.getText() == terminate_partition_expression:
                        is_partition = False
                        break
                else:
                    if is_partition:
                        partitions.append(nextchild.getText())

                index += 1
        return TableSource(name=table, partitions=partitions, alias=alias, indexHints=indexhint)

    def visitSubqueryTableItem(self, ctx):
        #TODO: GLOBAL - check if identifires have quotes
        select = self.visit(ctx.subquery())
        alias = Identifier(ctx.id_().getText())
        return SubqueryClause(select=select, alias=alias)

    def visitTableSourcesItem(self, ctx):
        return TableRefParenthClause(tableRefs=self.visit(ctx.table_sources()))

    def visitIndex_hint(self, ctx):
        pass #TODO

    def visitInnerJoin(self, ctx):
        right = self.hlpGetTableItem(ctx.table_source_item())
        jointype = ctx.getChild(0).getText().lower()
        (joincondition, columnsconditions, isnatural) = (None, None, False)
        if ctx.expression():
            joincondition = self.visit(ctx.expression())
        if ctx.USING():
            columnsconditions = self.visit(ctx.id_list())
        return right, jointype, isnatural, joincondition, columnsconditions
    
    def visitStraightJoin(self, ctx):
        right = self.hlpGetTableItem(ctx.table_source_item())
        jointype = "straight"
        (joincondition, columnsconditions, isnatural) = (None, None, False)
        if ctx.expression():
            joincondition = self.visit(ctx.expression())
        return right, jointype, isnatural, joincondition, columnsconditions

    def visitOuterJoin(self, ctx):
        right = self.hlpGetTableItem(ctx.table_source_item())
        jointype = ctx.getChild(0).getText().lower()
        (joincondition, columnsconditions, isnatural) = (None, None, False)
        if ctx.expression():
            joincondition = self.visit(ctx.expression())
        if ctx.USING():
            columnsconditions = self.visit(ctx.id_list())
        return right, jointype, isnatural, joincondition, columnsconditions
    
    def visitNaturalJoin(self, ctx):
        right = self.hlpGetTableItem(ctx.table_source_item())
        jointype = "straight"
        (joincondition, columnsconditions, isnatural) = (None, None, True)
        return right, jointype, isnatural, joincondition, columnsconditions

    def hlpGetTableItem(self, tbl_item_tree):
        tbl_item = self.visit(tbl_item_tree)
        if isinstance(tbl_item, list) == False:
            return [tbl_item]
        return tbl_item

    def visitSubquery(self, ctx):
        return self.visit(ctx.select_statement())
    #       DML Detailed statements help end
    #   DML Detailed statements end

    #   DML Select statement details start
    def visitQuery_expression(self, ctx):
        if ctx.query_specification():
            return self.visit(ctx.query_specification())

        return ctx.query_expression();

    def visitQuery_expression_nointo(self, ctx):
        if ctx.query_specification_nointo():
            return self.visit(ctx.query_specification_nointo())

        return ctx.query_expression_nointo();

    def visitQuery_specification(self, ctx):
        return self.CommonQuerySpecification(ctx, False)

    def visitQuery_specification_nointo(self, ctx):
        return self.CommonQuerySpecification(ctx, True)

    def CommonQuerySpecification(self, query_specification_ctx, is_nointo):
        #TODO: make "into outfile" construct
        #TODO: make spec_options
        (columns, from_clause, where_clauses) = (None, None, None)
        (group_clauses, having_clauses, order_clauses) = (None, None, None)
        (row_count, offset, export) = (None, None, None)
        ctx = query_specification_ctx

        columns = self.visit(ctx.select_list()) if ctx.select_list() else None
        if ctx.from_clause():
            from_clause, where_clauses, group_clauses, having_clauses = self.visit(ctx.from_clause())
        order_clauses = self.visit(ctx.order_by_clause()) if ctx.order_by_clause() else None
        row_count, offset = self.visit(ctx.limit_clause()) if ctx.limit_clause() else (None, None)

        if is_nointo == False:
            export = self.visit(ctx.select_into_expression()) if ctx.select_into_expression() else None
        node = SelectStatement(
            columns=columns,
            fromClause=from_clause,
            where=where_clauses,
            groupBy=group_clauses,
            orderByElems=order_clauses,
            having=having_clauses,
            limitLines=row_count,
            limitOffset=offset,
            export=export
        )

        return node

    def visitUnion_parenth(self, ctx):
        type_ = ctx.getChild(1)
        union_type = None
        if isinstance(type_, TerminalNode):
            union_type = type_.getText()
        stmt = self.visit(ctx.query_expression_nointo())

        return UnionClause(statement=stmt, unionType=union_type)

    def visitUnion_statement(self, ctx):
        type_ = ctx.getChild(1)
        union_type = None
        if isinstance(type_, TerminalNode):
            union_type = type_.getText()
        if ctx.query_specification_nointo():
            stmt = self.visit(ctx.query_specification_nointo())
        else:
            stmt = self.visit(ctx.query_expression_nointo())

        return UnionClause(statement=stmt, unionType=union_type)

    #       DML Select statement details help start
    def visitSelect_spec(self, ctx):
        pass #TODO

    def visitSelect_list(self, ctx):
        columns = []

        # Handle first symbol if it is a "*".
        star_position = 0
        first = ctx.getChild(star_position)
        if isinstance(first, TerminalNode):
            columns.append(ColumnClause(ColumnName(column=Star("*"))))
        
        index = 0
        child_count = len(ctx.select_list_elem())

        while(index < child_count):
            column = self.visit(ctx.select_list_elem(index))
            columns.append(column)
            index +=1
        return columns

    def visitSellistelAllCol(self, ctx):
        schema, table = self.visit(ctx.full_id())
        column = Star()
        elem = ColumnName(db=None, schema=schema, table=table, column=column)
        return ColumnClause(value=elem, alias=None)

    def visitSellistelCol(self, ctx):
        alias = Identifier(ctx.id_().getText()) if ctx.id_() else None
        elem = self.visit(ctx.full_column_name())
        return ColumnClause(value=elem, alias=alias)

    def visitSellistelFunc(self, ctx):
        alias = Identifier(ctx.id_().getText()) if ctx.id_() else None
        elem = self.visit(ctx.function_call())
        return ColumnClause(value=elem, alias=alias)

    def visitSellistelExpr(self, ctx):
        alias = Identifier(ctx.id_().getText()) if ctx.id_() else None
        elem = self.visit(ctx.expression())
        return ColumnClause(value=elem, alias=alias)

    def visitSelect_into_expression(self, ctx):
        pass #TODO

    def visitSelectIntoVars(self, ctx):
        var_list = []
        # VERY DEPEND ON GRAMMAR
        child_index = 1
        child_count = ctx.getChildCount()
        while child_index < child_count:
            curChild = ctx.getChild(child_index)
            if isinstance(curChild, TerminalNode):
                # TODO: check if possible get system vars?
                var_list.append(Variable(issystem=False, name=curChild.getText()))
            else:
                var_list.append(Identifier(name=curChild.getText()))
            child_index += 2

        return ExportVarList(variables=var_list)

    def visitSelectIntoDump(self, ctx):
        filename = ctx.STRING_LITERAL().getText()
        return ExportDumpFile(fileName=filename)

    def visitSelectIntoOutfile(self, ctx):
        return self.formExportTextFileOptions(ctx)

    def visitFrom_clause(self, ctx):
        tables = self.visit(ctx.table_sources())
        group_clauses = None
        where_clauses = None
        having_clauses = None
        clauses = []

        i = 0
        while(ctx.group_by_item(i)):
            item = self.visit(ctx.group_by_item(i))
            clauses.append(item)
            i += 1

        if len(clauses) > 0 :
            groupby_operator = None
            if ctx.ROLLUP():
                groupby_operator = GroupbyOperatorSimple(name="ROLLUP")
            group_clauses = GroupbyClause(values=clauses, operator=groupby_operator)

        if ctx.WHERE():
            where_clauses = WhereClause(value=self.visit(ctx.expression(0)))

        if ctx.HAVING():
            if ctx.WHERE():
                having_clauses = self.visit(ctx.expression(1))
            else:
                having_clauses = self.visit(ctx.expression(0))

        return FromClause(tableRefs=tables), where_clauses, group_clauses, having_clauses

    def visitGroup_by_item(self, ctx):
        expr = self.visit(ctx.expression())
        sorttype = None
        if ctx.getChildCount() > 1:
            sorttype = ctx.getChild(1).getText()
        return SortItem(expression=expr, sortType=sorttype)

    def visitLimit_clause(self, ctx):
        offset = None
        # Explicit OFFSET.
        if ctx.OFFSET():
            row_count = ctx.decimal_literal(0).getText()
            offset = ctx.decimal_literal(1).getText()
        # Implicit OFFSET.
        else:
            if len(ctx.decimal_literal()) > 1:
                offset = ctx.decimal_literal(0).getText()
                row_count = ctx.decimal_literal(1).getText()
            else:
                row_count = ctx.decimal_literal(0).getText()
        return row_count, offset
    #       DML Select statement details help end
    #   DML Select statement details end
    # DML branch end

    # TRANSACTION branch start
    def visitStart_transaction(self, ctx):
        pass #TODO

    def visitBegin_work(self, ctx):
        pass #TODO

    def visitCommit_work(self, ctx):
        pass #TODO

    def visitRollback_work(self, ctx):
        pass #TODO

    def visitSavepoint_statement(self, ctx):
        pass #TODO

    def visitRollback_statement(self, ctx):
        pass #TODO

    def visitRelease_statement(self, ctx):
        pass #TODO

    def visitLock_tables(self, ctx):
        pass #TODO

    def visitUnlock_tables(self, ctx):
        pass #TODO
    # TRANSACTION branch end

    # REPLICATION branch start
    #   Replication base start

    def visitChange_master(self, ctx):
        pass #TODO

    def visitChange_repl_filter(self, ctx):
        pass #TODO

    def visitPurge_binary_logs(self, ctx):
        pass #TODO

    def visitReset_master(self, ctx):
        pass #TODO

    def visitReset_slave(self, ctx):
        pass #TODO

    def visitStart_slave(self, ctx):
        pass #TODO

    def visitStop_slave(self, ctx):
        pass #TODO

    def visitStart_group_repl(self, ctx):
        pass #TODO

    def visitStop_group_repl(self, ctx):
        pass #TODO
    #   Replication base end

    #   Replication XA Transactions start
    def visitXa_start_transaction(self, ctx):
        pass #TODO

    def visitXa_end_transaction(self, ctx):
        pass #TODO

    def visitXa_prepare(self, ctx):
        pass #TODO

    def visitXa_commit_work(self, ctx):
        pass #TODO

    def visitXa_rollback_work(self, ctx):
        pass #TODO

    def visitXa_recover_work(self, ctx):
        pass #TODO
    #   Replication XA Transactions end

    # REPLICATION branch end

    # PREPARED branch start
    def visitPrepare_statement(self, ctx):
        pass #TODO

    def visitExecute_statement(self, ctx):
        pass #TODO

    def visitDeallocate_prepare(self, ctx):
        pass #TODO
    # PREPARED branch end

    # COMPOUND statements branch start
    def visitRoutine_body(self, ctx):
        return self.visit(ctx.getChild(0))

    def visitBlock_statement(self, ctx):
        label = ctx.id_(0).getText() if ctx.id_() else None
        body = []
        for decl_var in ctx.declare_variable():
            body.append(self.visit(decl_var))
        for decl_cond in ctx.declare_condition():
            body.append(self.visit(decl_cond))
        for decl_cur in ctx.declare_cursor():
            body.append(self.visit(decl_cur))
        for decl_handl in ctx.declare_handler():
            body.append(self.visit(decl_handl))
        for stmt in ctx.procedure_sql_statement():
            body.append(self.visit(stmt))
        return BlockQueryStatement(bodyStatements=body, label=label)

    def visitCase_statement(self, ctx):
        casevalue = None
        #VERY depend on grammar
        index = 1
        cnt_childs = ctx.getChildCount()
        if isinstance(ctx.getChild(index), TerminalNode) == False:
            if ctx.id_():
                casevalue = Identifier(ctx.id_().getText())
            else:
                casevalue = self.visit(ctx.getChild(index))
            index += 1
        (is_continue, is_else, is_when) = (True, False, False)
        (case_opt_cond, cur_stmt) = (None, None)
        (stmts, else_stmts, alternatives) = ([], [], [])
        while is_continue == True:
            if isinstance(ctx.getChild(index), TerminalNode) == True:
                # Save accumulate info
                if is_when == True:
                    alternatives.append(ConditionChoiceOption(condition=case_opt_cond, statements=stmts))
                    is_when = False
                if is_else == True:
                    is_else = False
                    else_stmts = stmts
                stmts = []
                # Analize next elem
                next_elem_text = ctx.getChild(index).getText().lower()
                if next_elem_text == "end":
                    if ctx.getChild(index + 1).getText().lower() == "case":
                        is_continue = False

                if next_elem_text == "else":
                    is_else = True

                if next_elem_text == "when":
                    index += 1
                    case_opt_cond = self.visit(ctx.getChild(index))
                    index += 1 # THEN
                    index += 1
                    cur_stmt = self.visit(ctx.getChild(index))
                    stmts.append(cur_stmt)
                    is_when = True
            else:
                cur_stmt = self.visit(ctx.getChild(index))
                stmts.append(cur_stmt)
            index += 1

        return CaseStatement(caseValue=casevalue, alternatives=alternatives, elseAlternativeStatements=else_stmts)

    def visitIf_statement(self, ctx):
        index = 1
        condition = self.visit(ctx.getChild(index))
        index += 1
        (is_continue, is_else, is_first_cond, is_elseif) = (True, False, True, False)
        (stmts, first_stmts, alternatives, else_stmts) = ([], [], [], [])
        (cur_stmt, elif_cond) = (None, None)
        while is_continue == True:
            if isinstance(ctx.getChild(index), TerminalNode) == True:
                # Save accumulate info
                if is_first_cond == True:
                    is_first_cond = False
                    first_stmts = stmts
                if is_elseif == True:
                    is_elseif = False
                    alternatives.append(ConditionChoiceOption(condition=elif_cond, statements=stmts))
                if is_else == True:
                    is_else = False
                    else_stmts = stmts
                stmts = []
                # Analize next elem
                next_elem_text = ctx.getChild(index).getText().lower()
                if next_elem_text == "end":
                    if ctx.getChild(index + 1).getText().lower() == "if":
                        is_continue = False

                if next_elem_text == "else":
                    is_else = True

                if next_elem_text == "elseif":
                    index += 1
                    elif_cond = self.visit(ctx.getChild(index))
                    index += 1 # THEN
                    index += 1
                    cur_stmt = self.visit(ctx.getChild(index))
                    stmts.append(cur_stmt)
                    is_elseif = True
            else:
                cur_stmt = self.visit(ctx.getChild(index))
                stmts.append(cur_stmt)
            index += 1

        return IfStatement(
            condition=condition, statements=first_stmts,
            alternatives=alternatives, 
            elseAlternativeStatements=else_stmts)

    def visitIterate_statement(self, ctx):
        return IterateStatement(label=Identifier(ctx.id_().getText()))

    def visitLeave_statement(self, ctx):
        return LeaveStatement(label=Identifier(ctx.id_().getText()))

    def visitLoop_statement(self, ctx):
        label = None
        statements = []
        if len(ctx.id_()) > 0:
            label = Identifier(ctx.id_(0).getText())
        for stmt in ctx.procedure_sql_statement():
            statements.append(self.visit(stmt))
        return LoopStatement(label=label, statements=statements)

    def visitRepeat_statement(self, ctx):
        return self.hlpCycle_statement(ctx, "repeat")

    def hlpCycle_statement(self, ctx, cycle_type):
        ret = None
        expr = self.visit(ctx.expression())
        label = None
        statements = []
        if len(ctx.id_()) > 0:
            label = Identifier(ctx.id_(0).getText())
        for stmt in ctx.procedure_sql_statement():
            statements.append(self.visit(stmt))
        if cycle_type == "repeat":
            ret = RepeatStatement(searchCondition=expr, label=label, statements=statements)
        if cycle_type == "while":
            ret = WhileStatement(searchCondition=expr, label=label, statements=statements)
        return ret

    def visitReturn_statement(self, ctx):
        return ReturnStatement(value=self.visit(ctx.expression()))

    def visitWhile_statement(self, ctx):
        return self.hlpCycle_statement(ctx, "while")

    def visitCursor_statement(self, ctx):
        name = Identifier(ctx.id_(0).getText())
        if ctx.CLOSE():
            return HandleCursorStatement(handleType="close", name=name)
        if ctx.OPEN():
            return HandleCursorStatement(handleType="open", name=name)
        variables = []
        variables = self.visit(ctx.id_list())
        return FetchCursorStatement(name=name, variables=variables)

    # Compound statements branch help start
    def visitDeclare_variable(self, ctx):
        variables = []
        for var in ctx.id_():
            variables.append(Identifier(var.getText()))
        datatype = self.visit(ctx.data_type())
        defaultval = self.visit(ctx.default_value())
        return DeclareVariable(variables=variables, dataType=datatype, defaultValue=defaultval)

    def visitDeclare_condition(self, ctx):
        name = Identifier(ctx.id_().getText())
        errorcode = int(ctx.DECIMAL().text) if ctx.DECIMAL() else None
        sqlstate = ctx.STRING_LITERAL().text if ctx.STRING_LITERAL() else None
        return DeclareCondition(name=name, errorCode=errorcode, sqlState=sqlstate)

    def visitDeclare_cursor(self, ctx):
        name = Identifier(ctx.id_().getText())
        select = self.visit(ctx.select_statement())
        return DeclareCursor(name=name, select=select)

    def visitDeclare_handler(self, ctx):
        action = ctx.getChild(1).getText() # VERY depend on Grammar
        conds = []
        for cond in ctx.handler_condition_value():
            conds.append(self.visit(cond))
        stmt = self.visit(ctx.compound_clause())
        return DeclareHandler(action=action, conditions=conds, statement=stmt)



    def visitHandler_condition_value(self, ctx):
        condtype = None
        value = None
        if ctx.DECIMAL():
            condtype = "errorcode"
            value = int(ctx.DECIMAL().getText())
        if ctx.SQLSTATE():
            condtype = "sqlstate"
            value = ctx.STRING_LITERAL().text
        if ctx.id_():
            condtype = "conditionname"
            value = ctx.id_().getText()
        if ctx.SQLWARNING():
            condtype = "sqlwarning"
        if ctx.FOUND():
            condtype = "notfound"
        if ctx.SQLEXCEPTION():
            condtype = "sqlexception"

        return HandlerCondition(conditiontype=condtype, value=value)
    # Compound statements branch help end
    # COMPOUND statements branch end

    # ADMINISTRATION statements branch start
    # ADMINISTRATION statements branch end

    # UTILITY statements branch start
    def visitSimple_describe_statement(self, ctx):
        #TODO: finished
        table = self.visit(ctx.table_name())
        return DescribeTable(table=table)

    def visitFull_describe_statement(self, ctx):
        pass #TODO

    def visitHelp_statement(self, ctx):
        pass #TODO

    def visitUse_statement(self, ctx):
        schema = ctx.id_().getText()
        return UseStatement(schema=schema)

    # UTILITY statements branch end

    # COMMON CLAUSES start
    #   Common, db objects' names start
    def visitTable_name(self, ctx):
        (schema, table) = self.hlpGetFullName(ctx)
        return TableName(db=None, schema=schema, table=table)

    def hlpGetFullName(self, ctx):
        (schema, obj) = (None, None)
        if ctx.getChildCount() > 1:
            if ctx.DOT_ID():
                schema = Identifier(ctx.id_(0).getText())
                obj = Identifier(ctx.DOT_ID().getText()[1:])
            else:
                schema = Identifier(ctx.id_(0).getText())
                obj = Identifier(ctx.id_(1).getText())
        else:
            obj = Identifier(ctx.id_(0).getText())
        return schema, obj

    def visitFull_id(self, ctx):
        return self.hlpGetFullName(ctx)

    def visitFull_column_name(self, ctx):
        schema = None
        table = None
        column = None
        dotExtId = ctx.dot_ext_id()
        cnt_DotExtId = len(dotExtId)
        if cnt_DotExtId == 2:
            # Schema, table and column
            schema = Identifier(ctx.id_().getText())
            table = Identifier(dotExtId[0].getText()[1:])
            column = Identifier(dotExtId[1].getText()[1:])
        elif cnt_DotExtId == 1:
            # Table and column.
            table = Identifier(ctx.id_().getText())
            column = Identifier(dotExtId[0].getText()[1:])
        else:
            # Only column.
            column = Identifier(ctx.id_().getText())

        return ColumnName(schema=schema, table=table, column=column)

    def visitIndex_col_name(self, ctx):
        colname = Identifier(ctx.id_().getText())
        length = int(ctx.decimal_literal().getText()) if ctx.decimal_literal() else None
        sorttype = "ASC" if ctx.ASC() else None
        sorttype = "DESC" if ctx.DESC() else sorttype
        
        return IndexColNameClause(
            columnName=Identifier(ctx.id_().getText()), length=length, sortType=sorttype)

    def visitUser_name(self, ctx):
        username = ctx.getText()
        if username.find('@') == -1:
            return UserName(name=username, host="")
        name = username[:username.index('@')]
        host = username[username.index('@') + 1:]
        
        return UserName(name=name, host=host)

    def visitMysql_variable(self, ctx):
        text = ctx.getText()
        if text[0:2] == "@@":
            is_system = True
            name = text[2:]
        else:
            is_system = False
            name = text[1:]

        return Variable(issystem=is_system, value=name)

    def visitCharset_name(self, ctx):
        pass

    def visitCollation_name(self, ctx):
        pass

    def visitEngine_name(self, ctx):
        pass
        
    def visitUuid_set(self, ctx):
        pass #TODO
        
    def visitXid(self, ctx):
        pass #TODO
        
    def visitXid_string_id(self, ctx):
        pass #TODO
        
    def visitAuth_plugin(self, ctx):
        pass #TODO
        
    def visitId_(self, ctx):
        pass
        
    def visitSimple_id(self, ctx):
        pass
        
    def visitDot_ext_id(self, ctx):
        pass
        
    #   Common, db objects' names end

    #   Common, Literals start
    def visitDecimal_literal(self, ctx):
        pass

    def visitFilesize_literal(self, ctx):
        pass #TODO
    
    def visitString_literal(self, ctx):
        pass #TODO: cast "str1" "str2" ... "strN"

    def visitBoolean_literal(self, ctx):
        pass

    def visitHexadecimal_literal(self, ctx):
        pass

    def visitNull_notnull(self, ctx):
        if ctx.NOT():
            return NotNullLiteral(value=ctx.getText())
        return NullLiteral(value=ctx.getText())

    def visitConstant(self, ctx):
        if ctx.string_literal():
            return StringLiteral(ctx.getText()[1:-1])
        if ctx.hexadecimal_literal():
            return HexadecimalLiteral(ctx.getText())
        if ctx.decimal_literal():
            return NumberLiteral(ctx.getText())
        if ctx.REAL_LITERAL():
            return RealLiteral(ctx.getText())
        if ctx.boolean_literal():
            return BooleanLiteral(ctx.getText())
        if ctx.BIT_STRING():
            return BitStringLiteral(ctx.getText())
        if ctx.NOT():
            return NotNullLiteral(value=ctx.getText())
        return NullLiteral(value=ctx.getText())
    #   Common, Literals end

    #   Common, DataTypes start
    def visitCharDatatype(self, ctx):
        typename = ctx.getChild(0).getText()
        length_tree = ctx.length_one_dimension()
        length = None
        isbinary = ctx.BINARY().getText() if ctx.BINARY() else None
        charsetname = CharSet(ctx.charset_name().getText()) if ctx.charset_name() else None
        collationname = ctx.collation_name().getText() if ctx.collation_name() else None
        if length_tree:
            length = length_tree.decimal_literal().getText()

        return CharDataTypeClause(
            typeName=typename, length=length, isBinary=isbinary, 
            charSetName=charsetname, collationName=collationname)

    def visitDimensionDatatype(self, ctx):
        typename = ctx.getChild(0).getText()
        length_tree = ctx.length_one_dimension()
        length = None
        secondlength = None
        isunsigned = True if ctx.UNSIGNED() else False
        iszerofill = True if ctx.ZEROFILL() else False

        if length_tree:
            length = length_tree.decimal_literal().getText()

        length_tree = ctx.length_two_dimension() if ctx.length_two_dimension() else ctx.length_two_optional_dimension()

        if length_tree:
            length = length_tree.decimal_literal(0).getText()
            if len(length_tree.decimal_literal()) > 1:
                secondlength = length_tree.decimal_literal(1).getText()

        return DimensionDataTypeClause(
            typeName=typename, length=length, secondLength=secondlength, 
            isUnsigned=isunsigned, isZerofill=iszerofill)

    def visitSimpleDatatype(self, ctx):
        return SimpleDataTypeClause(typeName=ctx.getChild(0).getText())

    def visitCollectCharDatatype(self, ctx):
        typename = ctx.getChild(0).getText()
        isbinary = ctx.BINARY().getText() if ctx.BINARY() else None
        charsetname = CharSet(ctx.charset_name().getText()) if ctx.charset_name() else None
        collationname = ctx.collation_name().getText() if ctx.collation_name() else None
        values = []
        values_tree = ctx.STRING_LITERAL()
        length_tree = len(values_tree)
        index = 0
        while index < length_tree:
            values.append(StringLiteral(values_tree[index].getText()[1:-1]))
            index += 1

        return CollectionCharDataTypeClause(
            typeName=typename, isBinary=isbinary, charSetName=charsetname, 
            collationName=collationname, values=values
            )

    def visitSpatialDatatype(self, ctx):
        return SimpleDataTypeClause(typeName=ctx.spatial_data_type().getText())

    def visitData_type_to_convert(self, ctx):
        datatype = ctx.getChild(0).getText()
        firstdim = None
        seconddim = None
        charset = None

        firstdim_tree = ctx.length_one_dimension()
        if firstdim_tree:
            firstdim = firstdim_tree.decimal_literal().getText()

        seconddim_tree = ctx.length_two_dimension()
        if seconddim_tree:
            firstdim = seconddim_tree.decimal_literal(0).getText()
            seconddim = seconddim_tree.decimal_literal(1).getText()

        if ctx.charset_name():
            charset = CharSet(ctx.charset_name().getText())

        return ConvertedDataType(
            dataType=datatype, firstDim=firstdim,
            secondDim=seconddim, charSet=charset)

    def visitSpatial_data_type(self, ctx):
        pass

    def visitLength_one_dimension(self, ctx):
        pass

    def visitLength_two_dimension(self, ctx):
        pass

    def visitLength_two_optional_dimension(self, ctx):
        pass
    #   Common, DataTypes end

    #   Common, Lists start
    def visitId_list(self, ctx):
        ids = []
        for next_id in ctx.id_():
            ids.append(Identifier(name=next_id.getText()))
        return ids

    def visitTable_list(self, ctx):
        pass #TODO

    def visitTable_pair_list(self, ctx):
        pass #TODO

    def visitIndex_colname_list(self, ctx):
        icols = []
        for next_icol in ctx.index_col_name():
            icols.append(self.visit(next_icol))

        return icols
    
    def visitExpression_list(self, ctx):
        exprs = []
        for next_expr in ctx.expression():
            exprs.append(self.visit(next_expr))

        return exprs

    def visitConstant_list(self, ctx):
        consts = []
        for next_const in ctx.constant():
            consts.append(self.visit(next_const))

        return consts

    def visitSimple_string_list(self, ctx):
        pass #TODO

    def visitUser_var_list(self, ctx):
        pass #TODO

    #   Common, Lists end

    #   Common, Expression start
    def visitDefault_value(self, ctx):
        defaultvalue = None
        if ctx.NULL_LITERAL():
            defaultvalue = NullLiteral(value="null")
        else:
            defaultvalue = self.visit(ctx.constant())
        return defaultvalue

    def visitIf_exists(self, ctx):
        pass

    def visitIf_not_exists(self, ctx):
        pass
    #   Common, Expression end

    #   Common, Functions start
    def visitSimpleSpecificFCall(self, ctx):
        name = ctx.getChild(0).getText()
        return NoParenthFunctionCall(name=name)

    def visitConvertDataTypeFCall(self, ctx):
        # mysql CONVERT() and CAST() functions.
        name = ctx.getChild(0).getText()
        extArgs = []
        extArg = None
        # Define first argument.
        curArg = self.visit(ctx.expression())
        extArgs.append(FuncExtExprArgument(value=curArg))
        
        # Second argument will be different in differnt type of sql.
        if ctx.USING():
            # Case with CONVERT( ... USING ...).
            curArg = CharSet(ctx.charset_name().getText())
            extArg = FuncExtCharsetArgument(value=curArg, keyword="USING", keywordPosition="BEFORE")
        elif ctx.AS():
            # Case with CAST(... AS ...).
            curArg = self.visit(ctx.data_type_to_convert())
            extArg = FuncExtDataTypeArgument(value=curArg, keyword="AS", keywordPosition="BEFORE")
        else:
            # Case with CONVERT(..., ...).
            curArg = self.visit(ctx.data_type_to_convert())
            extArg = FuncExtDataTypeArgument(value=curArg, separator=",")
        
        # Add constructed second argument.
        extArgs.append(extArg)

        return ExtArgFunctionCall(name=name, arguments=extArgs)

    def visitValuesFCall(self, ctx):
        # mysql VALUES() function.
        name = ctx.getChild(0).getText()
        arguments = []
        arg = self.visit(ctx.full_column_name())
        arguments.append(arg)

        return SimpleFunctionCall(name=name, arguments=arguments)

    def visitCaseFCall(self, ctx):
        expression = None
        cases = []
        elsecase = None
        funcArgCnt = None

        if ctx.expression():
            expression = self.visit(ctx.expression())

        index = 0
        cntCases = len(ctx.condarg)
        if cntCases != len(ctx.resarg):
            raise ValueError("Error! throw exception!")
            # TODO: throw exception
        while index < cntCases:
            when_ = self.visit(ctx.condarg[index])
            then_ = self.visit(ctx.resarg[index])
            cases.append(CaseClause(whenClause=when_, thenClause=then_))
            index += 1

        if ctx.ELSE():
            funcArgCnt = len(ctx.function_arg())
            elsecase = self.visit(ctx.function_arg(funcArgCnt - 1))


        return CaseFunctionCall(expression=expression, cases=cases, elseCase=elsecase)

    def visitCharFCall(self, ctx):
        # mysql CHAR() function.
        name = ctx.getChild(0).getText()
        arguments = []
        # Construct SpecArgs from massiv of SimpleArgs.
        # First iteration is separate, because we process arg1 in (arg1, arg2, ...).
        # Each next iteration processes construct: ',' arg_i
        args_tree = ctx.function_args()
        index = 0
        child_count = args_tree.getChildCount()
        nextchild = args_tree.getChild(index)
        arguments.append(FuncExtExprArgument(keyword=None, keywordPosition=None, value=self.visit(nextchild), separator=None))
        index += 1
        while index < child_count:
            nextchild = args_tree.getChild(index)
            if isinstance(nextchild, TerminalNode) == False:
                arguments.append(FuncExtExprArgument(keyword=None, keywordPosition=None, value=self.visit(nextchild), separator=','))
            index += 1
        
        if ctx.charset_name():
            arguments.append(FuncExtCharsetArgument(keyword="USING", keywordPosition="BEFORE", value=ctx.charset_name().getText()))

        return ExtArgFunctionCall(name=name, arguments=arguments)

    def visitPositionFCall(self, ctx):
        name = ctx.getChild(0).getText()
        firstarg = None
        secondarg = None
        arguments = []

        if ctx.fstr:
            firstarg = StringLiteral(ctx.fstr.getText()[1:-1])
        if ctx.sstr:
            secondarg = StringLiteral(ctx.sstr.getText()[1:-1])
        if ctx.fexpr:
            firstarg = self.visit(ctx.fexpr)
        if ctx.sexpr:
            secondarg = self.visit(ctx.sexpr)

        arguments.append(FuncExtExprArgument(value=firstarg))
        arguments.append(FuncExtExprArgument(value=secondarg, keyword="IN", keywordPosition="BEFORE"))
        return ExtArgFunctionCall(name=name, arguments=arguments)

    def visitSubstrFCall(self, ctx):
        name = ctx.getChild(0).getText()
        arguments = []
        curArg = None

        # Process first arg of substring.
        if ctx.string_literal():
            curArg = StringLiteral(ctx.string_literal().getText()[1:-1])

        if ctx.fexpr:
            curArg = self.visit(ctx.fexpr)

        arguments.append(FuncExtExprArgument(value=curArg))

        # Process second arg of substring.
        if ctx.fdecimal:
            curArg = NumberLiteral(ctx.fdecimal.getText())

        if ctx.sexpr:
            curArg = self.visit(ctx.sexpr)

        arguments.append(FuncExtExprArgument(value=curArg, keyword="FROM", keywordPosition="BEFORE"))

        # Process third arg of substring.
        curArg = None
        if ctx.sdecimal:
            curArg = NumberLiteral(ctx.sdecimal.getText())

        if ctx.texpr:
            curArg = self.visit(ctx.texpr)

        if curArg:
            arguments.append(FuncExtExprArgument(value=curArg, keyword="FOR", keywordPosition="BEFORE"))

        return ExtArgFunctionCall(name=name, arguments=arguments)

    def visitTrimFCall(self, ctx):
        name = ctx.getChild(0).getText()
        arguments = []
        keyword = None
        is_first_kw = False
        curArg = None

        # Check if we have only-keyword arg
        if ctx.BOTH():
            keyword = "BOTH"
            is_first_kw = True
        if ctx.LEADING():
            keyword = "LEADING"
            is_first_kw = True
        if ctx.TRAILING():
            keyword = "TRAILING"
            is_first_kw = True

        if is_first_kw:
            curArg = FuncExtKeywordArgument(keyword=keyword)
            arguments.append(curArg)

        # Process first arg of trim.
        curArg = None
        if ctx.fstr:
            curArg = StringLiteral(ctx.fstr.getText()[1:-1])

        if ctx.fexpr:
            curArg = self.visit(ctx.fexpr)

        if curArg:
            arguments.append(FuncExtExprArgument(value=curArg))

        # Process second arg of trim.
        if ctx.sstr:
            curArg = StringLiteral(ctx.sstr.getText()[1:-1])

        if ctx.sexpr:
            curArg = self.visit(ctx.sexpr)

        arguments.append(FuncExtExprArgument(value=curArg, keyword="FROM", keywordPosition="BEFORE"))

        return ExtArgFunctionCall(name=name, arguments=arguments)

    def visitWeightFCall(self, ctx):
        name = ctx.getChild(0).getText()
        arguments = []
        firstArg = None
        secondArg = None
        lastArg = None
        lastArgValues = None
        kw = None
        levelarg_tree = None

        if ctx.string_literal():
            firstArg = StringLiteral(ctx.string_literal().getText()[1:-1])

        if ctx.expression():
            firstArg = self.visit(ctx.expression())

        arguments.append(FuncExtExprArgument(value=firstArg))

        # if second arg is AS.
        if ctx.AS():
            secondArg = NumberLiteral(ctx.decimal_literal().getText())
            if ctx.CHAR():
                kw = "AS CHAR"
            else:
                kw = "AS BINARY"
            arguments.append(FuncExtExprArgument(keyword=kw, keywordPosition="BEFORE", value=secondArg))
        # if last arg is LEVEL.
        levelarg_tree = ctx.levels_in_weight_string()
        if levelarg_tree:
            lastArgValues = self.visit(levelarg_tree)
            lastArg = FuncExtNestedArgument(keyword="LEVEL", keywordPosition="BEFORE", values=lastArgValues)
            arguments.append(lastArg)

        return ExtArgFunctionCall(name=name, arguments=arguments)

    def visitLevelWeightFList(self, ctx):
        weightStrArgs = []
        nextKWOrd = None
        nextkwordPos = None
        nextval = None

        # process firstArg.
        if ctx.firstord:
            nextKWOrd = ctx.firstord.text
            nextkwordPos = "AFTER"
        nextval = ctx.firstlevel.getText()
        weightStrArgs.append(FuncExtExprArgument(keyword=nextKWOrd, keywordPosition=nextkwordPos, value=nextval))
        # Process OtherArgs.
        # TODO: make correct situation when len(nextLevel) != len(nextOrder)
        cntLevels = len(ctx.nextlevel)
        index = 0
        while index < cntLevels:
            nextval = ctx.nextlevel[index].getText()
            weightStrArgs.append(FuncExtExprArgument(value=nextval, separator=','))
            index += 1

        return weightStrArgs

    def visitLevelWeightFRange(self, ctx):
        weightStrArgs = []

        # Process firstArg.
        weightStrArgs.append(FuncExtExprArgument(value=ctx.firstlevel.getText()))
        # process secondArg.
        weightStrArgs.append(FuncExtExprArgument(value=ctx.lastlevel.getText(), separator='-'))

        return weightStrArgs

    def visitExtractFCall(self, ctx):
        name = ctx.getChild(0).getText()
        arguments = []
        curArg = None

        # Process interval_type.
        curArg = ctx.interval_type().getText()
        arguments.append(FuncExtKeywordArgument(keyword=curArg))

        # Process second arg.
        if ctx.fstr:
            curArg = StringLiteral(ctx.fstr.getText()[1:-1])

        if ctx.fexpr:
            curArg = self.visit(ctx.fexpr)

        arguments.append(FuncExtExprArgument(value=curArg, keyword="FROM", keywordPosition="BEFORE"))

        return ExtArgFunctionCall(name=name, arguments=arguments)


    def visitGetFormatFCall(self, ctx):
        # It very depends on grammar.
        name = ctx.getChild(0).getText()
        firstarg_position = 2
        arguments = []
        arguments.append(FuncExtKeywordArgument(keyword=ctx.getChild(firstarg_position).getText()))
        arguments.append(FuncExtExprArgument(value=StringLiteral(ctx.string_literal().getText()[1:-1]), separator=","))

        return ExtArgFunctionCall(name=name, arguments=arguments)

    def visitAggregateFunctionCall(self, ctx):
        return self.visit(ctx.aggregate_windowed_function())

    def visitScalarFunctionCall(self, ctx):
        # processing objects scalar_function_name and function_args here
        name = ctx.scalar_function_name().getText()
        arguments = None
        if ctx.function_args():
            arguments = self.visit(ctx.function_args())
        return SimpleFunctionCall(name=name, arguments=arguments)

    def visitUdfFunctionCall(self, ctx):
        schema, routine = self.visit(ctx.full_id())
        udfName = UDFuncName(db=None, schema=schema, routine=routine)
        arguments = None
        if ctx.function_args():
            arguments = self.visit(ctx.function_args())
        return UDFFunctionCall(name=udfName, arguments=arguments)

    def visitLevels_in_weight_string(self, ctx):
        pass

    def visitAggregate_windowed_function(self, ctx):
        name = ctx.getChild(0).getText()
        aggregator = None
        arguments = None
        orderby = None
        concatseparator = None

        if ctx.ALL():
            aggregator = "ALL"
        if ctx.DISTINCT():
            aggregator = "DISTINCT"

        if ctx.function_arg():
            arguments = []
            arguments.append(self.visit(ctx.function_arg()))

        if ctx.function_args():
            arguments = self.visit(ctx.function_args())

        if ctx.order_by_expression():
            orderby = []
            orderby_size = len(ctx.order_by_expression())
            index = 0
            while index < orderby_size:
                orderby.append(self.visit(ctx.order_by_expression(index)))
                index += 1

        # Very depends on grammar.
        if ctx.STRING_LITERAL():
            concatseparator = ctx.STRING_LITERAL().getText()[1:-1]

        return AggregateFunctionCall(
            name=name, aggregator=aggregator, arguments=arguments, 
            orderByElems=orderby, concatSeparator=concatseparator)

    def visitScalar_function_name(self, ctx):
        pass

    def visitFunction_args(self, ctx):
        arguments = []
        index = 0
        cnt_childs = ctx.getChildCount()
        while index < cnt_childs:
            nextchild = ctx.getChild(index)
            if isinstance(nextchild, TerminalNode) == False:
                arguments.append(self.visit(nextchild))
            index += 1
        return arguments

    def visitFunction_arg(self, ctx):
        return self.visit(ctx.getChild(0))
    #   Common, Functions end

    #   Common, Expressions start
    def visitNotExpression(self, ctx):
        left = self.visit(ctx.expression())
        return(LogicalExpression(isUnary=True, operator="NOT", leftArg=left))

    def visitLogicalExpression(self, ctx):
        first = 0
        second = 1
        left = self.visit(ctx.expression(first))
        right = self.visit(ctx.expression(second))
        operator = ctx.logical_operator().getText()
        return LogicalExpression(isUnary=False, operator=operator, leftArg=left, rightArg=right)

    def visitIsExpression(self, ctx):
        logicalmatch = None
        isnot = True if ctx.NOT() else False
        value = self.visit(ctx.predicate())
        logicalmatch_position = 2
        if isnot:
            logicalmatch_position += 1
        logicalmatch = ctx.getChild(logicalmatch_position).getText()
        return IsExpression(isNot=isnot, value=value, logicalMatch=logicalmatch)

    def visitPredicateExpression(self, ctx):
        first = 0
        predicate = ctx.getChild(first)
        return self.visit(ctx.predicate())

    def visitInPredicate(self, ctx):
        subquery = None
        value = self.visit(ctx.predicate())
        values = []
        issubquery = False
        isnot = True if ctx.NOT() else False
        
        subquery_tree = ctx.subquery()
        if subquery_tree:
            issubquery = True
            subquery = self.visit(subquery_tree)

        expression_list_tree = ctx.expression_list()
        if expression_list_tree:
            values = self.visit(expression_list_tree)

        return InPredicate(
            isSubquery=issubquery, isNot=isnot, subquery=subquery, 
            comparableValue=value, comparedValues=values
        )

    def visitIsNullPredicate(self, ctx):
        value = self.visit(ctx.predicate())
        isnot = False
        if ctx.null_notnull().NOT():
            isnot = True
        return IsNullPredicate(isNot=isnot, value=value)

    def visitBinaryComparasionPredicate(self, ctx):
        comparisonoperator = ctx.comparison_operator().getText()
        first = 0
        second = 1
        left = self.visit(ctx.predicate(first))
        right = self.visit(ctx.predicate(second))
        return ComparisonPredicate(comparisonOperator=comparisonoperator, leftArg=left , rightArg=right)

    def visitSubqueryComparasionPredicate(self, ctx):
        comparisonoperator = ctx.comparison_operator().getText()
        num_typeof_all_any_literal = 2
        choisetype = ctx.getChild(num_typeof_all_any_literal).getText()
        value = self.visit(ctx.predicate())
        subquery = self.visit(ctx.subquery())
        return ComparisonSetPredicate(comparisonOperator=comparisonoperator, quantifierType=choisetype, value=value, subquery=subquery)

    def visitBetweenPredicate(self, ctx):
        value = self.visit(ctx.predicate(0))
        left  = self.visit(ctx.predicate(1))
        right = self.visit(ctx.predicate(2))
        isnot = True if ctx.NOT() else False
        return BetweenPredicate(isNot=isnot, value=value, leftArg=left, rightArg=right)

    def visitSoundsLikePredicate(self, ctx):
        typelike = "SOUNDS"
        value = self.visit(ctx.predicate(0))
        pattern = self.visit(ctx.predicate(1))
        return LikePredicate(typeLike=typelike, value=value, pattern=pattern)

    def visitLikePredicate(self, ctx):
        typelike = "LIKE"
        value = self.visit(ctx.predicate(0))
        pattern = self.visit(ctx.predicate(1))
        isnot = True if ctx.NOT() else False
        escape = ctx.string_literal.getText()[1:-1] if ctx.ESCAPE() else None
        return LikePredicate(isNot=isnot, typeLike=typelike, value=value, pattern=pattern, escapeString=escape)

    def visitRegexpPredicate(self, ctx):
        typelike = "REGEXP" if ctx.REGEXP() else "RLIKE"
        isnot = True if ctx.NOT() else False
        value = self.visit(ctx.predicate(0))
        pattern = self.visit(ctx.predicate(1))
        return LikePredicate(isNot=isnot, typeLike=typelike, value=value, pattern=pattern)
        
    def visitExpressionAtomPredicate(self, ctx):
        return self.visit(ctx.expression_atom())

    ## ExpressionAtom start.
    def visitDefaultExpressionAtom(self, ctx):
        return KeywordPrimitive("DEFAULT")
        
    def visitFullColumnNameExpressionAtom(self, ctx):
        return self.visit(ctx.full_column_name())

    def visitMysqlVariableExpressionAtom(self, ctx):
        text = ctx.mysql_variable().getText()
        if text[0:2] == "@@":
            return Variable(issystem=True, name=text[2:])
        else:
            return Variable(issystem=False, name=text[1:])
        
    def visitUnaryExpressionAtom(self, ctx):
        expr = self.visit(ctx.expression_atom())
        op = ctx.unary_operator().getText()
        return UnaryExpression(op, expr)
        
    def visitBinaryExpressionAtom(self, ctx):
        value = self.visit(ctx.expression_atom())
        return StringPrimitive(transformationType="BINARY", value=value)

    def visitNestedExpressionAtom(self, ctx):
        return ParenthesisExpression(self.visit(ctx.expression()))

    def visitExistsExpessionAtom(self, ctx):
        if ctx.EXISTS():
            return ExistsExpression(self.visit(ctx.subquery()))
        return SubqueryExpression(self.visit(ctx.subquery()))

    def visitIntervalExpressionAtom(self, ctx):
        type_ = ctx.interval_type().getText()
        value = self.visit(ctx.expression())
        return IntervalExpression(intervalType=type_, value=value)
    
    def visitBitExpressionAtom(self, ctx):
        left = self.visit(ctx.expression_atom(0))
        right = self.visit(ctx.expression_atom(1))
        op = ctx.bit_operator().getText()
        return BinaryExpression(operation=op, leftArg=left, rightArg=right)

    def visitMathExpressionAtom(self, ctx):
        left = self.visit(ctx.expression_atom(0))
        right = self.visit(ctx.expression_atom(1))
        op = ctx.math_operator().getText()
        return BinaryExpression(operation=op, leftArg=left, rightArg=right)
    
    def visitConstantExpressionAtom(self, ctx):
        return self.visit(ctx.constant())

    def visitUnary_operator(self, ctx):
        pass

    def visitComparison_operator(self, ctx):
        pass
        
    def visitLogical_operator(self, ctx):
        pass
        
    def visitBit_operator(self, ctx):
        pass
        
    def visitMath_operator(self, ctx):
        pass
    #   Common, Expressions end

    #   Common, Simple id set start
    def visitCharset_name_base(self, ctx):
        pass
        
    def visitTransaction_level_base(self, ctx):
        pass
        
    def visitPrivileges_base(self, ctx):
        pass
        
    def visitInterval_type_base(self, ctx):
        pass
        
    def visitData_type_base(self, ctx):
        pass
        
    def visitKeywords_can_be_id(self, ctx):
        pass
        
    def visitFunction_name_base(self, ctx):
        pass
    #   Common, Simple id set end
