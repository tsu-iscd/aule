# Generated from mysqlParser.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .mysqlParser import mysqlParser
else:
    from mysqlParser import mysqlParser

# This class defines a complete generic visitor for a parse tree produced by mysqlParser.

class mysqlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by mysqlParser#root.
    def visitRoot(self, ctx:mysqlParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#sqlStatements.
    def visitSqlStatements(self, ctx:mysqlParser.SqlStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#sqlStatement.
    def visitSqlStatement(self, ctx:mysqlParser.SqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#emptyStatement.
    def visitEmptyStatement(self, ctx:mysqlParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#ddlStatement.
    def visitDdlStatement(self, ctx:mysqlParser.DdlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dmlStatement.
    def visitDmlStatement(self, ctx:mysqlParser.DmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#transactionStatement.
    def visitTransactionStatement(self, ctx:mysqlParser.TransactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#replicationStatement.
    def visitReplicationStatement(self, ctx:mysqlParser.ReplicationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#preparedStatement.
    def visitPreparedStatement(self, ctx:mysqlParser.PreparedStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#compoundStatement.
    def visitCompoundStatement(self, ctx:mysqlParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#administrationStatement.
    def visitAdministrationStatement(self, ctx:mysqlParser.AdministrationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#utilityStatement.
    def visitUtilityStatement(self, ctx:mysqlParser.UtilityStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#createDatabase.
    def visitCreateDatabase(self, ctx:mysqlParser.CreateDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#createEvent.
    def visitCreateEvent(self, ctx:mysqlParser.CreateEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#createIndex.
    def visitCreateIndex(self, ctx:mysqlParser.CreateIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#createLogfileGroup.
    def visitCreateLogfileGroup(self, ctx:mysqlParser.CreateLogfileGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#createProcedure.
    def visitCreateProcedure(self, ctx:mysqlParser.CreateProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#createFunction.
    def visitCreateFunction(self, ctx:mysqlParser.CreateFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#createServer.
    def visitCreateServer(self, ctx:mysqlParser.CreateServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#copyCreateTable.
    def visitCopyCreateTable(self, ctx:mysqlParser.CopyCreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#queryCreateTable.
    def visitQueryCreateTable(self, ctx:mysqlParser.QueryCreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#columnCreateTable.
    def visitColumnCreateTable(self, ctx:mysqlParser.ColumnCreateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#createTablespaceInnodb.
    def visitCreateTablespaceInnodb(self, ctx:mysqlParser.CreateTablespaceInnodbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#createTablespaceNdb.
    def visitCreateTablespaceNdb(self, ctx:mysqlParser.CreateTablespaceNdbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#createTrigger.
    def visitCreateTrigger(self, ctx:mysqlParser.CreateTriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#createView.
    def visitCreateView(self, ctx:mysqlParser.CreateViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#createDatabaseOption.
    def visitCreateDatabaseOption(self, ctx:mysqlParser.CreateDatabaseOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#ownerStatement.
    def visitOwnerStatement(self, ctx:mysqlParser.OwnerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#preciseSchedule.
    def visitPreciseSchedule(self, ctx:mysqlParser.PreciseScheduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#intervalSchedule.
    def visitIntervalSchedule(self, ctx:mysqlParser.IntervalScheduleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#timestampValue.
    def visitTimestampValue(self, ctx:mysqlParser.TimestampValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#intervalExpr.
    def visitIntervalExpr(self, ctx:mysqlParser.IntervalExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#intervalType.
    def visitIntervalType(self, ctx:mysqlParser.IntervalTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#enableType.
    def visitEnableType(self, ctx:mysqlParser.EnableTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#indexType.
    def visitIndexType(self, ctx:mysqlParser.IndexTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#indexOption.
    def visitIndexOption(self, ctx:mysqlParser.IndexOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#procedureParameter.
    def visitProcedureParameter(self, ctx:mysqlParser.ProcedureParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#functionParameter.
    def visitFunctionParameter(self, ctx:mysqlParser.FunctionParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#routineComment.
    def visitRoutineComment(self, ctx:mysqlParser.RoutineCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#routineLanguage.
    def visitRoutineLanguage(self, ctx:mysqlParser.RoutineLanguageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#routineBehavior.
    def visitRoutineBehavior(self, ctx:mysqlParser.RoutineBehaviorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#routineData.
    def visitRoutineData(self, ctx:mysqlParser.RoutineDataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#routineSecurity.
    def visitRoutineSecurity(self, ctx:mysqlParser.RoutineSecurityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#serverOption.
    def visitServerOption(self, ctx:mysqlParser.ServerOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#createDefinitions.
    def visitCreateDefinitions(self, ctx:mysqlParser.CreateDefinitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#columnDeclaration.
    def visitColumnDeclaration(self, ctx:mysqlParser.ColumnDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#constraintDeclaration.
    def visitConstraintDeclaration(self, ctx:mysqlParser.ConstraintDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#indexDeclaration.
    def visitIndexDeclaration(self, ctx:mysqlParser.IndexDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#columnDefinition.
    def visitColumnDefinition(self, ctx:mysqlParser.ColumnDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#nullColumnConstraint.
    def visitNullColumnConstraint(self, ctx:mysqlParser.NullColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#defaultColumnConstraint.
    def visitDefaultColumnConstraint(self, ctx:mysqlParser.DefaultColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#autoIncrementColumnConstraint.
    def visitAutoIncrementColumnConstraint(self, ctx:mysqlParser.AutoIncrementColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#primaryKeyColumnConstraint.
    def visitPrimaryKeyColumnConstraint(self, ctx:mysqlParser.PrimaryKeyColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#uniqueKeyColumnConstraint.
    def visitUniqueKeyColumnConstraint(self, ctx:mysqlParser.UniqueKeyColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#commentColumnConstraint.
    def visitCommentColumnConstraint(self, ctx:mysqlParser.CommentColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#formatColumnConstraint.
    def visitFormatColumnConstraint(self, ctx:mysqlParser.FormatColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#storageColumnConstraint.
    def visitStorageColumnConstraint(self, ctx:mysqlParser.StorageColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#referenceColumnConstraint.
    def visitReferenceColumnConstraint(self, ctx:mysqlParser.ReferenceColumnConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#primaryKeyTableConstraint.
    def visitPrimaryKeyTableConstraint(self, ctx:mysqlParser.PrimaryKeyTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#uniqueKeyTableConstraint.
    def visitUniqueKeyTableConstraint(self, ctx:mysqlParser.UniqueKeyTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#foreignKeyTableConstraint.
    def visitForeignKeyTableConstraint(self, ctx:mysqlParser.ForeignKeyTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#checkTableConstraint.
    def visitCheckTableConstraint(self, ctx:mysqlParser.CheckTableConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#referenceDefinition.
    def visitReferenceDefinition(self, ctx:mysqlParser.ReferenceDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#referenceAction.
    def visitReferenceAction(self, ctx:mysqlParser.ReferenceActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#referenceControlType.
    def visitReferenceControlType(self, ctx:mysqlParser.ReferenceControlTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#simpleIndexDeclaration.
    def visitSimpleIndexDeclaration(self, ctx:mysqlParser.SimpleIndexDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#specialIndexDeclaration.
    def visitSpecialIndexDeclaration(self, ctx:mysqlParser.SpecialIndexDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionEngine.
    def visitTableOptionEngine(self, ctx:mysqlParser.TableOptionEngineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionAutoIncrement.
    def visitTableOptionAutoIncrement(self, ctx:mysqlParser.TableOptionAutoIncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionAverage.
    def visitTableOptionAverage(self, ctx:mysqlParser.TableOptionAverageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionCharset.
    def visitTableOptionCharset(self, ctx:mysqlParser.TableOptionCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionChecksum.
    def visitTableOptionChecksum(self, ctx:mysqlParser.TableOptionChecksumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionCollate.
    def visitTableOptionCollate(self, ctx:mysqlParser.TableOptionCollateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionComment.
    def visitTableOptionComment(self, ctx:mysqlParser.TableOptionCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionCompression.
    def visitTableOptionCompression(self, ctx:mysqlParser.TableOptionCompressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionConnection.
    def visitTableOptionConnection(self, ctx:mysqlParser.TableOptionConnectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionDataDirectory.
    def visitTableOptionDataDirectory(self, ctx:mysqlParser.TableOptionDataDirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionDelay.
    def visitTableOptionDelay(self, ctx:mysqlParser.TableOptionDelayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionEncryption.
    def visitTableOptionEncryption(self, ctx:mysqlParser.TableOptionEncryptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionIndexDirectory.
    def visitTableOptionIndexDirectory(self, ctx:mysqlParser.TableOptionIndexDirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionInsertMethod.
    def visitTableOptionInsertMethod(self, ctx:mysqlParser.TableOptionInsertMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionKeyBlockSize.
    def visitTableOptionKeyBlockSize(self, ctx:mysqlParser.TableOptionKeyBlockSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionMaxRows.
    def visitTableOptionMaxRows(self, ctx:mysqlParser.TableOptionMaxRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionMinRows.
    def visitTableOptionMinRows(self, ctx:mysqlParser.TableOptionMinRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionPackKeys.
    def visitTableOptionPackKeys(self, ctx:mysqlParser.TableOptionPackKeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionPassword.
    def visitTableOptionPassword(self, ctx:mysqlParser.TableOptionPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionRowFormat.
    def visitTableOptionRowFormat(self, ctx:mysqlParser.TableOptionRowFormatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionRecalculation.
    def visitTableOptionRecalculation(self, ctx:mysqlParser.TableOptionRecalculationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionPersistent.
    def visitTableOptionPersistent(self, ctx:mysqlParser.TableOptionPersistentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionSamplePage.
    def visitTableOptionSamplePage(self, ctx:mysqlParser.TableOptionSamplePageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionTablespace.
    def visitTableOptionTablespace(self, ctx:mysqlParser.TableOptionTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableOptionUnion.
    def visitTableOptionUnion(self, ctx:mysqlParser.TableOptionUnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tablespaceStorage.
    def visitTablespaceStorage(self, ctx:mysqlParser.TablespaceStorageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#partitionDefinitions.
    def visitPartitionDefinitions(self, ctx:mysqlParser.PartitionDefinitionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#partitionFunctionHash.
    def visitPartitionFunctionHash(self, ctx:mysqlParser.PartitionFunctionHashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#partitionFunctionKey.
    def visitPartitionFunctionKey(self, ctx:mysqlParser.PartitionFunctionKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#partitionFunctionRange.
    def visitPartitionFunctionRange(self, ctx:mysqlParser.PartitionFunctionRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#partitionFunctionList.
    def visitPartitionFunctionList(self, ctx:mysqlParser.PartitionFunctionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#subPartitionFunctionHash.
    def visitSubPartitionFunctionHash(self, ctx:mysqlParser.SubPartitionFunctionHashContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#subPartitionFunctionKey.
    def visitSubPartitionFunctionKey(self, ctx:mysqlParser.SubPartitionFunctionKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#partitionComparision.
    def visitPartitionComparision(self, ctx:mysqlParser.PartitionComparisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#partitionList.
    def visitPartitionList(self, ctx:mysqlParser.PartitionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#partitionSimple.
    def visitPartitionSimple(self, ctx:mysqlParser.PartitionSimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#subpartitionDefinition.
    def visitSubpartitionDefinition(self, ctx:mysqlParser.SubpartitionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#partitionOptionEngine.
    def visitPartitionOptionEngine(self, ctx:mysqlParser.PartitionOptionEngineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#partitionOptionComment.
    def visitPartitionOptionComment(self, ctx:mysqlParser.PartitionOptionCommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#partitionOptionDataDirectory.
    def visitPartitionOptionDataDirectory(self, ctx:mysqlParser.PartitionOptionDataDirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#partitionOptionIndexDirectory.
    def visitPartitionOptionIndexDirectory(self, ctx:mysqlParser.PartitionOptionIndexDirectoryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#partitionOptionMaxRows.
    def visitPartitionOptionMaxRows(self, ctx:mysqlParser.PartitionOptionMaxRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#partitionOptionMinRows.
    def visitPartitionOptionMinRows(self, ctx:mysqlParser.PartitionOptionMinRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#partitionOptionTablespace.
    def visitPartitionOptionTablespace(self, ctx:mysqlParser.PartitionOptionTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#partitionOptionNodeGroup.
    def visitPartitionOptionNodeGroup(self, ctx:mysqlParser.PartitionOptionNodeGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterSimpleDatabase.
    def visitAlterSimpleDatabase(self, ctx:mysqlParser.AlterSimpleDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterUpgradeName.
    def visitAlterUpgradeName(self, ctx:mysqlParser.AlterUpgradeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterEvent.
    def visitAlterEvent(self, ctx:mysqlParser.AlterEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterFunction.
    def visitAlterFunction(self, ctx:mysqlParser.AlterFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterInstance.
    def visitAlterInstance(self, ctx:mysqlParser.AlterInstanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterLogfileGroup.
    def visitAlterLogfileGroup(self, ctx:mysqlParser.AlterLogfileGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterProcedure.
    def visitAlterProcedure(self, ctx:mysqlParser.AlterProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterServer.
    def visitAlterServer(self, ctx:mysqlParser.AlterServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterTable.
    def visitAlterTable(self, ctx:mysqlParser.AlterTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterTablespace.
    def visitAlterTablespace(self, ctx:mysqlParser.AlterTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterView.
    def visitAlterView(self, ctx:mysqlParser.AlterViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterTableOption.
    def visitAlterTableOption(self, ctx:mysqlParser.AlterTableOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByAddColumn.
    def visitAlterByAddColumn(self, ctx:mysqlParser.AlterByAddColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByAddColumns.
    def visitAlterByAddColumns(self, ctx:mysqlParser.AlterByAddColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByAddIndex.
    def visitAlterByAddIndex(self, ctx:mysqlParser.AlterByAddIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByAddPrimaryKey.
    def visitAlterByAddPrimaryKey(self, ctx:mysqlParser.AlterByAddPrimaryKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByAddUniqueKey.
    def visitAlterByAddUniqueKey(self, ctx:mysqlParser.AlterByAddUniqueKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByAddSpecialIndex.
    def visitAlterByAddSpecialIndex(self, ctx:mysqlParser.AlterByAddSpecialIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByAddForeignKey.
    def visitAlterByAddForeignKey(self, ctx:mysqlParser.AlterByAddForeignKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterTableAlgorighm.
    def visitAlterTableAlgorighm(self, ctx:mysqlParser.AlterTableAlgorighmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByChangeDefault.
    def visitAlterByChangeDefault(self, ctx:mysqlParser.AlterByChangeDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByChangeColumn.
    def visitAlterByChangeColumn(self, ctx:mysqlParser.AlterByChangeColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByLock.
    def visitAlterByLock(self, ctx:mysqlParser.AlterByLockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByModifyColumn.
    def visitAlterByModifyColumn(self, ctx:mysqlParser.AlterByModifyColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByDropColumn.
    def visitAlterByDropColumn(self, ctx:mysqlParser.AlterByDropColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByDropPrimaryKey.
    def visitAlterByDropPrimaryKey(self, ctx:mysqlParser.AlterByDropPrimaryKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByDropIndex.
    def visitAlterByDropIndex(self, ctx:mysqlParser.AlterByDropIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByDropForeignKey.
    def visitAlterByDropForeignKey(self, ctx:mysqlParser.AlterByDropForeignKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByDisableKeys.
    def visitAlterByDisableKeys(self, ctx:mysqlParser.AlterByDisableKeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByEnableKeys.
    def visitAlterByEnableKeys(self, ctx:mysqlParser.AlterByEnableKeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByRename.
    def visitAlterByRename(self, ctx:mysqlParser.AlterByRenameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByOrder.
    def visitAlterByOrder(self, ctx:mysqlParser.AlterByOrderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByConvertCharset.
    def visitAlterByConvertCharset(self, ctx:mysqlParser.AlterByConvertCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterTableDefaultCharset.
    def visitAlterTableDefaultCharset(self, ctx:mysqlParser.AlterTableDefaultCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByDiscardTablespace.
    def visitAlterByDiscardTablespace(self, ctx:mysqlParser.AlterByDiscardTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByImportTablespace.
    def visitAlterByImportTablespace(self, ctx:mysqlParser.AlterByImportTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByForce.
    def visitAlterByForce(self, ctx:mysqlParser.AlterByForceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByValidate.
    def visitAlterByValidate(self, ctx:mysqlParser.AlterByValidateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByAddPartition.
    def visitAlterByAddPartition(self, ctx:mysqlParser.AlterByAddPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByDropPartition.
    def visitAlterByDropPartition(self, ctx:mysqlParser.AlterByDropPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByDiscardPartition.
    def visitAlterByDiscardPartition(self, ctx:mysqlParser.AlterByDiscardPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByImportPartition.
    def visitAlterByImportPartition(self, ctx:mysqlParser.AlterByImportPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByTruncatePartition.
    def visitAlterByTruncatePartition(self, ctx:mysqlParser.AlterByTruncatePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByCoalescePartition.
    def visitAlterByCoalescePartition(self, ctx:mysqlParser.AlterByCoalescePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByReorganizePartition.
    def visitAlterByReorganizePartition(self, ctx:mysqlParser.AlterByReorganizePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByExchangePartition.
    def visitAlterByExchangePartition(self, ctx:mysqlParser.AlterByExchangePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByAnalyzePartitiion.
    def visitAlterByAnalyzePartitiion(self, ctx:mysqlParser.AlterByAnalyzePartitiionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByCheckPartition.
    def visitAlterByCheckPartition(self, ctx:mysqlParser.AlterByCheckPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByOptimizePartition.
    def visitAlterByOptimizePartition(self, ctx:mysqlParser.AlterByOptimizePartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByRebuildPartition.
    def visitAlterByRebuildPartition(self, ctx:mysqlParser.AlterByRebuildPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByRepairPartition.
    def visitAlterByRepairPartition(self, ctx:mysqlParser.AlterByRepairPartitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByRemovePartitioning.
    def visitAlterByRemovePartitioning(self, ctx:mysqlParser.AlterByRemovePartitioningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterByUpgradePartitioning.
    def visitAlterByUpgradePartitioning(self, ctx:mysqlParser.AlterByUpgradePartitioningContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dropDatabase.
    def visitDropDatabase(self, ctx:mysqlParser.DropDatabaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dropEvent.
    def visitDropEvent(self, ctx:mysqlParser.DropEventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dropIndex.
    def visitDropIndex(self, ctx:mysqlParser.DropIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dropLogfileGroup.
    def visitDropLogfileGroup(self, ctx:mysqlParser.DropLogfileGroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dropProcedure.
    def visitDropProcedure(self, ctx:mysqlParser.DropProcedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dropFunction.
    def visitDropFunction(self, ctx:mysqlParser.DropFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dropServer.
    def visitDropServer(self, ctx:mysqlParser.DropServerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dropTable.
    def visitDropTable(self, ctx:mysqlParser.DropTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dropTablespace.
    def visitDropTablespace(self, ctx:mysqlParser.DropTablespaceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dropTrigger.
    def visitDropTrigger(self, ctx:mysqlParser.DropTriggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dropView.
    def visitDropView(self, ctx:mysqlParser.DropViewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#renameTable.
    def visitRenameTable(self, ctx:mysqlParser.RenameTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#truncateTable.
    def visitTruncateTable(self, ctx:mysqlParser.TruncateTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#callStatement.
    def visitCallStatement(self, ctx:mysqlParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#deleteStatement.
    def visitDeleteStatement(self, ctx:mysqlParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#doStatement.
    def visitDoStatement(self, ctx:mysqlParser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#handlerStatement.
    def visitHandlerStatement(self, ctx:mysqlParser.HandlerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#insertStatement.
    def visitInsertStatement(self, ctx:mysqlParser.InsertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#loadDataStatement.
    def visitLoadDataStatement(self, ctx:mysqlParser.LoadDataStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#loadXmlStatement.
    def visitLoadXmlStatement(self, ctx:mysqlParser.LoadXmlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#replaceStatement.
    def visitReplaceStatement(self, ctx:mysqlParser.ReplaceStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#simpleSelect.
    def visitSimpleSelect(self, ctx:mysqlParser.SimpleSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#parenthesisSelect.
    def visitParenthesisSelect(self, ctx:mysqlParser.ParenthesisSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#unionSelect.
    def visitUnionSelect(self, ctx:mysqlParser.UnionSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#unionParenthesisSelect.
    def visitUnionParenthesisSelect(self, ctx:mysqlParser.UnionParenthesisSelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#updateStatement.
    def visitUpdateStatement(self, ctx:mysqlParser.UpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#insertStatementValue.
    def visitInsertStatementValue(self, ctx:mysqlParser.InsertStatementValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#updatedElement.
    def visitUpdatedElement(self, ctx:mysqlParser.UpdatedElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#assignmentField.
    def visitAssignmentField(self, ctx:mysqlParser.AssignmentFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#lockClause.
    def visitLockClause(self, ctx:mysqlParser.LockClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#singleDeleteStatement.
    def visitSingleDeleteStatement(self, ctx:mysqlParser.SingleDeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#multipleDeleteStatement.
    def visitMultipleDeleteStatement(self, ctx:mysqlParser.MultipleDeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#handlerOpenStatement.
    def visitHandlerOpenStatement(self, ctx:mysqlParser.HandlerOpenStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#handlerReadIndexStatement.
    def visitHandlerReadIndexStatement(self, ctx:mysqlParser.HandlerReadIndexStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#handlerReadStatement.
    def visitHandlerReadStatement(self, ctx:mysqlParser.HandlerReadStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#handlerCloseStatement.
    def visitHandlerCloseStatement(self, ctx:mysqlParser.HandlerCloseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#singleUpdateStatement.
    def visitSingleUpdateStatement(self, ctx:mysqlParser.SingleUpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#multipleUpdateStatement.
    def visitMultipleUpdateStatement(self, ctx:mysqlParser.MultipleUpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#orderByClause.
    def visitOrderByClause(self, ctx:mysqlParser.OrderByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#orderByExpression.
    def visitOrderByExpression(self, ctx:mysqlParser.OrderByExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableSources.
    def visitTableSources(self, ctx:mysqlParser.TableSourcesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableSource.
    def visitTableSource(self, ctx:mysqlParser.TableSourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#atomTableItem.
    def visitAtomTableItem(self, ctx:mysqlParser.AtomTableItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#subqueryTableItem.
    def visitSubqueryTableItem(self, ctx:mysqlParser.SubqueryTableItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableSourcesItem.
    def visitTableSourcesItem(self, ctx:mysqlParser.TableSourcesItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#indexHint.
    def visitIndexHint(self, ctx:mysqlParser.IndexHintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#indexHintType.
    def visitIndexHintType(self, ctx:mysqlParser.IndexHintTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#innerJoin.
    def visitInnerJoin(self, ctx:mysqlParser.InnerJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#straightJoin.
    def visitStraightJoin(self, ctx:mysqlParser.StraightJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#outerJoin.
    def visitOuterJoin(self, ctx:mysqlParser.OuterJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#naturalJoin.
    def visitNaturalJoin(self, ctx:mysqlParser.NaturalJoinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#subquery.
    def visitSubquery(self, ctx:mysqlParser.SubqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#queryExpression.
    def visitQueryExpression(self, ctx:mysqlParser.QueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#queryExpressionNointo.
    def visitQueryExpressionNointo(self, ctx:mysqlParser.QueryExpressionNointoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#querySpecification.
    def visitQuerySpecification(self, ctx:mysqlParser.QuerySpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#querySpecificationNointo.
    def visitQuerySpecificationNointo(self, ctx:mysqlParser.QuerySpecificationNointoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#unionParenthesis.
    def visitUnionParenthesis(self, ctx:mysqlParser.UnionParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#unionStatement.
    def visitUnionStatement(self, ctx:mysqlParser.UnionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#selectSpec.
    def visitSelectSpec(self, ctx:mysqlParser.SelectSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#selectElements.
    def visitSelectElements(self, ctx:mysqlParser.SelectElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#selectStarElement.
    def visitSelectStarElement(self, ctx:mysqlParser.SelectStarElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#selectColumnElement.
    def visitSelectColumnElement(self, ctx:mysqlParser.SelectColumnElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#selectFunctionElement.
    def visitSelectFunctionElement(self, ctx:mysqlParser.SelectFunctionElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#selectExpressionElement.
    def visitSelectExpressionElement(self, ctx:mysqlParser.SelectExpressionElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#selectIntoVariables.
    def visitSelectIntoVariables(self, ctx:mysqlParser.SelectIntoVariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#selectIntoDumpFile.
    def visitSelectIntoDumpFile(self, ctx:mysqlParser.SelectIntoDumpFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#selectIntoTextFile.
    def visitSelectIntoTextFile(self, ctx:mysqlParser.SelectIntoTextFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#fromClause.
    def visitFromClause(self, ctx:mysqlParser.FromClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#groupByItem.
    def visitGroupByItem(self, ctx:mysqlParser.GroupByItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#limitClause.
    def visitLimitClause(self, ctx:mysqlParser.LimitClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#startTransaction.
    def visitStartTransaction(self, ctx:mysqlParser.StartTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#beginWork.
    def visitBeginWork(self, ctx:mysqlParser.BeginWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#commitWork.
    def visitCommitWork(self, ctx:mysqlParser.CommitWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#rollbackWork.
    def visitRollbackWork(self, ctx:mysqlParser.RollbackWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#savepointStatement.
    def visitSavepointStatement(self, ctx:mysqlParser.SavepointStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#rollbackStatement.
    def visitRollbackStatement(self, ctx:mysqlParser.RollbackStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#releaseStatement.
    def visitReleaseStatement(self, ctx:mysqlParser.ReleaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#lockTables.
    def visitLockTables(self, ctx:mysqlParser.LockTablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#unlockTables.
    def visitUnlockTables(self, ctx:mysqlParser.UnlockTablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#setAutocommitStatement.
    def visitSetAutocommitStatement(self, ctx:mysqlParser.SetAutocommitStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#setTransactionStatement.
    def visitSetTransactionStatement(self, ctx:mysqlParser.SetTransactionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#transactionMode.
    def visitTransactionMode(self, ctx:mysqlParser.TransactionModeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#lockTableElement.
    def visitLockTableElement(self, ctx:mysqlParser.LockTableElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#lockAction.
    def visitLockAction(self, ctx:mysqlParser.LockActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#transactionOption.
    def visitTransactionOption(self, ctx:mysqlParser.TransactionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#transactionLevel.
    def visitTransactionLevel(self, ctx:mysqlParser.TransactionLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#changeMaster.
    def visitChangeMaster(self, ctx:mysqlParser.ChangeMasterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#changeReplicationFilter.
    def visitChangeReplicationFilter(self, ctx:mysqlParser.ChangeReplicationFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#purgeBinaryLogs.
    def visitPurgeBinaryLogs(self, ctx:mysqlParser.PurgeBinaryLogsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#resetMaster.
    def visitResetMaster(self, ctx:mysqlParser.ResetMasterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#resetSlave.
    def visitResetSlave(self, ctx:mysqlParser.ResetSlaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#startSlave.
    def visitStartSlave(self, ctx:mysqlParser.StartSlaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#stopSlave.
    def visitStopSlave(self, ctx:mysqlParser.StopSlaveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#startGroupReplication.
    def visitStartGroupReplication(self, ctx:mysqlParser.StartGroupReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#stopGroupReplication.
    def visitStopGroupReplication(self, ctx:mysqlParser.StopGroupReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#masterStringOption.
    def visitMasterStringOption(self, ctx:mysqlParser.MasterStringOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#masterDecimalOption.
    def visitMasterDecimalOption(self, ctx:mysqlParser.MasterDecimalOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#masterBoolOption.
    def visitMasterBoolOption(self, ctx:mysqlParser.MasterBoolOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#masterRealOption.
    def visitMasterRealOption(self, ctx:mysqlParser.MasterRealOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#masterUidListOption.
    def visitMasterUidListOption(self, ctx:mysqlParser.MasterUidListOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#stringMasterOption.
    def visitStringMasterOption(self, ctx:mysqlParser.StringMasterOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#decimalMasterOption.
    def visitDecimalMasterOption(self, ctx:mysqlParser.DecimalMasterOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#boolMasterOption.
    def visitBoolMasterOption(self, ctx:mysqlParser.BoolMasterOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#channelOption.
    def visitChannelOption(self, ctx:mysqlParser.ChannelOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#doDbReplication.
    def visitDoDbReplication(self, ctx:mysqlParser.DoDbReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#ignoreDbReplication.
    def visitIgnoreDbReplication(self, ctx:mysqlParser.IgnoreDbReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#doTableReplication.
    def visitDoTableReplication(self, ctx:mysqlParser.DoTableReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#ignoreTableReplication.
    def visitIgnoreTableReplication(self, ctx:mysqlParser.IgnoreTableReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#wildDoTableReplication.
    def visitWildDoTableReplication(self, ctx:mysqlParser.WildDoTableReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#wildIgnoreTableReplication.
    def visitWildIgnoreTableReplication(self, ctx:mysqlParser.WildIgnoreTableReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#rewriteDbReplication.
    def visitRewriteDbReplication(self, ctx:mysqlParser.RewriteDbReplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#threadType.
    def visitThreadType(self, ctx:mysqlParser.ThreadTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#gtidsUntilOption.
    def visitGtidsUntilOption(self, ctx:mysqlParser.GtidsUntilOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#masterLogUntilOption.
    def visitMasterLogUntilOption(self, ctx:mysqlParser.MasterLogUntilOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#relayLogUntilOption.
    def visitRelayLogUntilOption(self, ctx:mysqlParser.RelayLogUntilOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#sqlGapsUntilOption.
    def visitSqlGapsUntilOption(self, ctx:mysqlParser.SqlGapsUntilOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#connectionOption.
    def visitConnectionOption(self, ctx:mysqlParser.ConnectionOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#gtuidSet.
    def visitGtuidSet(self, ctx:mysqlParser.GtuidSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#xaStartTransaction.
    def visitXaStartTransaction(self, ctx:mysqlParser.XaStartTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#xaEndTransaction.
    def visitXaEndTransaction(self, ctx:mysqlParser.XaEndTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#xaPrepareStatement.
    def visitXaPrepareStatement(self, ctx:mysqlParser.XaPrepareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#xaCommitWork.
    def visitXaCommitWork(self, ctx:mysqlParser.XaCommitWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#xaRollbackWork.
    def visitXaRollbackWork(self, ctx:mysqlParser.XaRollbackWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#xaRecoverWork.
    def visitXaRecoverWork(self, ctx:mysqlParser.XaRecoverWorkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#prepareStatement.
    def visitPrepareStatement(self, ctx:mysqlParser.PrepareStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#executeStatement.
    def visitExecuteStatement(self, ctx:mysqlParser.ExecuteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#deallocatePrepare.
    def visitDeallocatePrepare(self, ctx:mysqlParser.DeallocatePrepareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#routineBody.
    def visitRoutineBody(self, ctx:mysqlParser.RoutineBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#blockStatement.
    def visitBlockStatement(self, ctx:mysqlParser.BlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#caseStatement.
    def visitCaseStatement(self, ctx:mysqlParser.CaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#ifStatement.
    def visitIfStatement(self, ctx:mysqlParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#iterateStatement.
    def visitIterateStatement(self, ctx:mysqlParser.IterateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#leaveStatement.
    def visitLeaveStatement(self, ctx:mysqlParser.LeaveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#loopStatement.
    def visitLoopStatement(self, ctx:mysqlParser.LoopStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#repeatStatement.
    def visitRepeatStatement(self, ctx:mysqlParser.RepeatStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#returnStatement.
    def visitReturnStatement(self, ctx:mysqlParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#whileStatement.
    def visitWhileStatement(self, ctx:mysqlParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#CloseCursor.
    def visitCloseCursor(self, ctx:mysqlParser.CloseCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#FetchCursor.
    def visitFetchCursor(self, ctx:mysqlParser.FetchCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#OpenCursor.
    def visitOpenCursor(self, ctx:mysqlParser.OpenCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#declareVariable.
    def visitDeclareVariable(self, ctx:mysqlParser.DeclareVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#declareCondition.
    def visitDeclareCondition(self, ctx:mysqlParser.DeclareConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#declareCursor.
    def visitDeclareCursor(self, ctx:mysqlParser.DeclareCursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#declareHandler.
    def visitDeclareHandler(self, ctx:mysqlParser.DeclareHandlerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#handlerConditionValue.
    def visitHandlerConditionValue(self, ctx:mysqlParser.HandlerConditionValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#procedureSqlStatement.
    def visitProcedureSqlStatement(self, ctx:mysqlParser.ProcedureSqlStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#caseAlternative.
    def visitCaseAlternative(self, ctx:mysqlParser.CaseAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#elifAlternative.
    def visitElifAlternative(self, ctx:mysqlParser.ElifAlternativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterUserMysqlV56.
    def visitAlterUserMysqlV56(self, ctx:mysqlParser.AlterUserMysqlV56Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#alterUserMysqlV57.
    def visitAlterUserMysqlV57(self, ctx:mysqlParser.AlterUserMysqlV57Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#createUserMysqlV56.
    def visitCreateUserMysqlV56(self, ctx:mysqlParser.CreateUserMysqlV56Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#createUserMysqlV57.
    def visitCreateUserMysqlV57(self, ctx:mysqlParser.CreateUserMysqlV57Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dropUser.
    def visitDropUser(self, ctx:mysqlParser.DropUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#grantStatement.
    def visitGrantStatement(self, ctx:mysqlParser.GrantStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#grantProxy.
    def visitGrantProxy(self, ctx:mysqlParser.GrantProxyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#renameUser.
    def visitRenameUser(self, ctx:mysqlParser.RenameUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#detailRevoke.
    def visitDetailRevoke(self, ctx:mysqlParser.DetailRevokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#shortRevoke.
    def visitShortRevoke(self, ctx:mysqlParser.ShortRevokeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#revokeProxy.
    def visitRevokeProxy(self, ctx:mysqlParser.RevokeProxyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#setPasswordStatement.
    def visitSetPasswordStatement(self, ctx:mysqlParser.SetPasswordStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#userPasswordOption.
    def visitUserPasswordOption(self, ctx:mysqlParser.UserPasswordOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#passwordAuthOption.
    def visitPasswordAuthOption(self, ctx:mysqlParser.PasswordAuthOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#stringAuthOption.
    def visitStringAuthOption(self, ctx:mysqlParser.StringAuthOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#hashAuthOption.
    def visitHashAuthOption(self, ctx:mysqlParser.HashAuthOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tlsOption.
    def visitTlsOption(self, ctx:mysqlParser.TlsOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#userResourceOption.
    def visitUserResourceOption(self, ctx:mysqlParser.UserResourceOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#userLockOption.
    def visitUserLockOption(self, ctx:mysqlParser.UserLockOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#privelegeClause.
    def visitPrivelegeClause(self, ctx:mysqlParser.PrivelegeClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#privilege.
    def visitPrivilege(self, ctx:mysqlParser.PrivilegeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#privilegeLevel.
    def visitPrivilegeLevel(self, ctx:mysqlParser.PrivilegeLevelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#analyzeTable.
    def visitAnalyzeTable(self, ctx:mysqlParser.AnalyzeTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#checkTable.
    def visitCheckTable(self, ctx:mysqlParser.CheckTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#checksumTable.
    def visitChecksumTable(self, ctx:mysqlParser.ChecksumTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#optimizeTable.
    def visitOptimizeTable(self, ctx:mysqlParser.OptimizeTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#repairTable.
    def visitRepairTable(self, ctx:mysqlParser.RepairTableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#checkTableOption.
    def visitCheckTableOption(self, ctx:mysqlParser.CheckTableOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#createUdfunction.
    def visitCreateUdfunction(self, ctx:mysqlParser.CreateUdfunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#installPlugin.
    def visitInstallPlugin(self, ctx:mysqlParser.InstallPluginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#uninstallPlugin.
    def visitUninstallPlugin(self, ctx:mysqlParser.UninstallPluginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#setVariable.
    def visitSetVariable(self, ctx:mysqlParser.SetVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#setCharset.
    def visitSetCharset(self, ctx:mysqlParser.SetCharsetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#setNames.
    def visitSetNames(self, ctx:mysqlParser.SetNamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#setPassword.
    def visitSetPassword(self, ctx:mysqlParser.SetPasswordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#setTransaction.
    def visitSetTransaction(self, ctx:mysqlParser.SetTransactionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#setAutocommit.
    def visitSetAutocommit(self, ctx:mysqlParser.SetAutocommitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showMasterLogs.
    def visitShowMasterLogs(self, ctx:mysqlParser.ShowMasterLogsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showLogEvents.
    def visitShowLogEvents(self, ctx:mysqlParser.ShowLogEventsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showObjectFilter.
    def visitShowObjectFilter(self, ctx:mysqlParser.ShowObjectFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showColumns.
    def visitShowColumns(self, ctx:mysqlParser.ShowColumnsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showCreateDb.
    def visitShowCreateDb(self, ctx:mysqlParser.ShowCreateDbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showCreateFullIdObject.
    def visitShowCreateFullIdObject(self, ctx:mysqlParser.ShowCreateFullIdObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showCreateUser.
    def visitShowCreateUser(self, ctx:mysqlParser.ShowCreateUserContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showEngine.
    def visitShowEngine(self, ctx:mysqlParser.ShowEngineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showGlobalInfo.
    def visitShowGlobalInfo(self, ctx:mysqlParser.ShowGlobalInfoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showErrors.
    def visitShowErrors(self, ctx:mysqlParser.ShowErrorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showCountErrors.
    def visitShowCountErrors(self, ctx:mysqlParser.ShowCountErrorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showSchemaFilter.
    def visitShowSchemaFilter(self, ctx:mysqlParser.ShowSchemaFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showRoutine.
    def visitShowRoutine(self, ctx:mysqlParser.ShowRoutineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showGrants.
    def visitShowGrants(self, ctx:mysqlParser.ShowGrantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showIndexes.
    def visitShowIndexes(self, ctx:mysqlParser.ShowIndexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showOpenTables.
    def visitShowOpenTables(self, ctx:mysqlParser.ShowOpenTablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showProfile.
    def visitShowProfile(self, ctx:mysqlParser.ShowProfileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showSlaveStatus.
    def visitShowSlaveStatus(self, ctx:mysqlParser.ShowSlaveStatusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#variableClause.
    def visitVariableClause(self, ctx:mysqlParser.VariableClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showCommonEntity.
    def visitShowCommonEntity(self, ctx:mysqlParser.ShowCommonEntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showFilter.
    def visitShowFilter(self, ctx:mysqlParser.ShowFilterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showGlobalInfoClause.
    def visitShowGlobalInfoClause(self, ctx:mysqlParser.ShowGlobalInfoClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showSchemaEntity.
    def visitShowSchemaEntity(self, ctx:mysqlParser.ShowSchemaEntityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#showProfileType.
    def visitShowProfileType(self, ctx:mysqlParser.ShowProfileTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#binlogStatement.
    def visitBinlogStatement(self, ctx:mysqlParser.BinlogStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#cacheIndexStatement.
    def visitCacheIndexStatement(self, ctx:mysqlParser.CacheIndexStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#flushStatement.
    def visitFlushStatement(self, ctx:mysqlParser.FlushStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#killStatement.
    def visitKillStatement(self, ctx:mysqlParser.KillStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#loadIndexIntoCache.
    def visitLoadIndexIntoCache(self, ctx:mysqlParser.LoadIndexIntoCacheContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#resetStatement.
    def visitResetStatement(self, ctx:mysqlParser.ResetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#shutdownStatement.
    def visitShutdownStatement(self, ctx:mysqlParser.ShutdownStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableIndexes.
    def visitTableIndexes(self, ctx:mysqlParser.TableIndexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#simpleFlushOption.
    def visitSimpleFlushOption(self, ctx:mysqlParser.SimpleFlushOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#channelFlushOption.
    def visitChannelFlushOption(self, ctx:mysqlParser.ChannelFlushOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableFlushOption.
    def visitTableFlushOption(self, ctx:mysqlParser.TableFlushOptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#loadedTableIndexes.
    def visitLoadedTableIndexes(self, ctx:mysqlParser.LoadedTableIndexesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#simpleDescribeStatement.
    def visitSimpleDescribeStatement(self, ctx:mysqlParser.SimpleDescribeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#fullDescribeStatement.
    def visitFullDescribeStatement(self, ctx:mysqlParser.FullDescribeStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#helpStatement.
    def visitHelpStatement(self, ctx:mysqlParser.HelpStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#useStatement.
    def visitUseStatement(self, ctx:mysqlParser.UseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#describeStatements.
    def visitDescribeStatements(self, ctx:mysqlParser.DescribeStatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#describeConnection.
    def visitDescribeConnection(self, ctx:mysqlParser.DescribeConnectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#fullId.
    def visitFullId(self, ctx:mysqlParser.FullIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tableName.
    def visitTableName(self, ctx:mysqlParser.TableNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#fullColumnName.
    def visitFullColumnName(self, ctx:mysqlParser.FullColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#indexColumnName.
    def visitIndexColumnName(self, ctx:mysqlParser.IndexColumnNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#userName.
    def visitUserName(self, ctx:mysqlParser.UserNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#mysqlVariable.
    def visitMysqlVariable(self, ctx:mysqlParser.MysqlVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#charsetName.
    def visitCharsetName(self, ctx:mysqlParser.CharsetNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#collationName.
    def visitCollationName(self, ctx:mysqlParser.CollationNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#engineName.
    def visitEngineName(self, ctx:mysqlParser.EngineNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#uuidSet.
    def visitUuidSet(self, ctx:mysqlParser.UuidSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#xid.
    def visitXid(self, ctx:mysqlParser.XidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#xuidStringId.
    def visitXuidStringId(self, ctx:mysqlParser.XuidStringIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#authPlugin.
    def visitAuthPlugin(self, ctx:mysqlParser.AuthPluginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#uid.
    def visitUid(self, ctx:mysqlParser.UidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#simpleId.
    def visitSimpleId(self, ctx:mysqlParser.SimpleIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dottedId.
    def visitDottedId(self, ctx:mysqlParser.DottedIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#decimalLiteral.
    def visitDecimalLiteral(self, ctx:mysqlParser.DecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#fileSizeLiteral.
    def visitFileSizeLiteral(self, ctx:mysqlParser.FileSizeLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#stringLiteral.
    def visitStringLiteral(self, ctx:mysqlParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#booleanLiteral.
    def visitBooleanLiteral(self, ctx:mysqlParser.BooleanLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#hexadecimalLiteral.
    def visitHexadecimalLiteral(self, ctx:mysqlParser.HexadecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#nullNotnull.
    def visitNullNotnull(self, ctx:mysqlParser.NullNotnullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#constant.
    def visitConstant(self, ctx:mysqlParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#stringDataType.
    def visitStringDataType(self, ctx:mysqlParser.StringDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dimensionDataType.
    def visitDimensionDataType(self, ctx:mysqlParser.DimensionDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#simpleDataType.
    def visitSimpleDataType(self, ctx:mysqlParser.SimpleDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#collectionDataType.
    def visitCollectionDataType(self, ctx:mysqlParser.CollectionDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#spatialDataType.
    def visitSpatialDataType(self, ctx:mysqlParser.SpatialDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#convertedDataType.
    def visitConvertedDataType(self, ctx:mysqlParser.ConvertedDataTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#lengthOneDimension.
    def visitLengthOneDimension(self, ctx:mysqlParser.LengthOneDimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#lengthTwoDimension.
    def visitLengthTwoDimension(self, ctx:mysqlParser.LengthTwoDimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#lengthTwoOptionalDimension.
    def visitLengthTwoOptionalDimension(self, ctx:mysqlParser.LengthTwoOptionalDimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#uidList.
    def visitUidList(self, ctx:mysqlParser.UidListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tables.
    def visitTables(self, ctx:mysqlParser.TablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#tablePairs.
    def visitTablePairs(self, ctx:mysqlParser.TablePairsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#indexColumnNames.
    def visitIndexColumnNames(self, ctx:mysqlParser.IndexColumnNamesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#expressions.
    def visitExpressions(self, ctx:mysqlParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#constants.
    def visitConstants(self, ctx:mysqlParser.ConstantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#simpleStrings.
    def visitSimpleStrings(self, ctx:mysqlParser.SimpleStringsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#userVariables.
    def visitUserVariables(self, ctx:mysqlParser.UserVariablesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#defaultValue.
    def visitDefaultValue(self, ctx:mysqlParser.DefaultValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#ifExists.
    def visitIfExists(self, ctx:mysqlParser.IfExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#ifNotExists.
    def visitIfNotExists(self, ctx:mysqlParser.IfNotExistsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#specificFunctionCall.
    def visitSpecificFunctionCall(self, ctx:mysqlParser.SpecificFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#aggregateFunctionCall.
    def visitAggregateFunctionCall(self, ctx:mysqlParser.AggregateFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#scalarFunctionCall.
    def visitScalarFunctionCall(self, ctx:mysqlParser.ScalarFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#udfFunctionCall.
    def visitUdfFunctionCall(self, ctx:mysqlParser.UdfFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#passwordFunctionCall.
    def visitPasswordFunctionCall(self, ctx:mysqlParser.PasswordFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#simpleFunctionCall.
    def visitSimpleFunctionCall(self, ctx:mysqlParser.SimpleFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dataTypeFunctionCall.
    def visitDataTypeFunctionCall(self, ctx:mysqlParser.DataTypeFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#valuesFunctionCall.
    def visitValuesFunctionCall(self, ctx:mysqlParser.ValuesFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#caseFunctionCall.
    def visitCaseFunctionCall(self, ctx:mysqlParser.CaseFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#charFunctionCall.
    def visitCharFunctionCall(self, ctx:mysqlParser.CharFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#positionFunctionCall.
    def visitPositionFunctionCall(self, ctx:mysqlParser.PositionFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#substrFunctionCall.
    def visitSubstrFunctionCall(self, ctx:mysqlParser.SubstrFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#trimFunctionCall.
    def visitTrimFunctionCall(self, ctx:mysqlParser.TrimFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#weightFunctionCall.
    def visitWeightFunctionCall(self, ctx:mysqlParser.WeightFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#extractFunctionCall.
    def visitExtractFunctionCall(self, ctx:mysqlParser.ExtractFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#getFormatFunctionCall.
    def visitGetFormatFunctionCall(self, ctx:mysqlParser.GetFormatFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#levelWeightList.
    def visitLevelWeightList(self, ctx:mysqlParser.LevelWeightListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#levelWeightRange.
    def visitLevelWeightRange(self, ctx:mysqlParser.LevelWeightRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#aggregateWindowedFunction.
    def visitAggregateWindowedFunction(self, ctx:mysqlParser.AggregateWindowedFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#scalarFunctionName.
    def visitScalarFunctionName(self, ctx:mysqlParser.ScalarFunctionNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#passwordFunctionClause.
    def visitPasswordFunctionClause(self, ctx:mysqlParser.PasswordFunctionClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#functionArgs.
    def visitFunctionArgs(self, ctx:mysqlParser.FunctionArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#functionArg.
    def visitFunctionArg(self, ctx:mysqlParser.FunctionArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#isExpression.
    def visitIsExpression(self, ctx:mysqlParser.IsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#notExpression.
    def visitNotExpression(self, ctx:mysqlParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#logicalExpression.
    def visitLogicalExpression(self, ctx:mysqlParser.LogicalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#predicateExpression.
    def visitPredicateExpression(self, ctx:mysqlParser.PredicateExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#soundsLikePredicate.
    def visitSoundsLikePredicate(self, ctx:mysqlParser.SoundsLikePredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#expressionAtomPredicate.
    def visitExpressionAtomPredicate(self, ctx:mysqlParser.ExpressionAtomPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#inPredicate.
    def visitInPredicate(self, ctx:mysqlParser.InPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#subqueryComparasionPredicate.
    def visitSubqueryComparasionPredicate(self, ctx:mysqlParser.SubqueryComparasionPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#betweenPredicate.
    def visitBetweenPredicate(self, ctx:mysqlParser.BetweenPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#binaryComparasionPredicate.
    def visitBinaryComparasionPredicate(self, ctx:mysqlParser.BinaryComparasionPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#isNullPredicate.
    def visitIsNullPredicate(self, ctx:mysqlParser.IsNullPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#likePredicate.
    def visitLikePredicate(self, ctx:mysqlParser.LikePredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#regexpPredicate.
    def visitRegexpPredicate(self, ctx:mysqlParser.RegexpPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#unaryExpressionAtom.
    def visitUnaryExpressionAtom(self, ctx:mysqlParser.UnaryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#existsExpessionAtom.
    def visitExistsExpessionAtom(self, ctx:mysqlParser.ExistsExpessionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#constantExpressionAtom.
    def visitConstantExpressionAtom(self, ctx:mysqlParser.ConstantExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#functionCallExpressionAtom.
    def visitFunctionCallExpressionAtom(self, ctx:mysqlParser.FunctionCallExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#mysqlVariableExpressionAtom.
    def visitMysqlVariableExpressionAtom(self, ctx:mysqlParser.MysqlVariableExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#binaryExpressionAtom.
    def visitBinaryExpressionAtom(self, ctx:mysqlParser.BinaryExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#fullColumnNameExpressionAtom.
    def visitFullColumnNameExpressionAtom(self, ctx:mysqlParser.FullColumnNameExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#defaultExpressionAtom.
    def visitDefaultExpressionAtom(self, ctx:mysqlParser.DefaultExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#bitExpressionAtom.
    def visitBitExpressionAtom(self, ctx:mysqlParser.BitExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#nestedExpressionAtom.
    def visitNestedExpressionAtom(self, ctx:mysqlParser.NestedExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#mathExpressionAtom.
    def visitMathExpressionAtom(self, ctx:mysqlParser.MathExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#intervalExpressionAtom.
    def visitIntervalExpressionAtom(self, ctx:mysqlParser.IntervalExpressionAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#unaryOperator.
    def visitUnaryOperator(self, ctx:mysqlParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:mysqlParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#logicalOperator.
    def visitLogicalOperator(self, ctx:mysqlParser.LogicalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#bitOperator.
    def visitBitOperator(self, ctx:mysqlParser.BitOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#mathOperator.
    def visitMathOperator(self, ctx:mysqlParser.MathOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#charsetNameBase.
    def visitCharsetNameBase(self, ctx:mysqlParser.CharsetNameBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#transactionLevelBase.
    def visitTransactionLevelBase(self, ctx:mysqlParser.TransactionLevelBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#privilegesBase.
    def visitPrivilegesBase(self, ctx:mysqlParser.PrivilegesBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#intervalTypeBase.
    def visitIntervalTypeBase(self, ctx:mysqlParser.IntervalTypeBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#dataTypeBase.
    def visitDataTypeBase(self, ctx:mysqlParser.DataTypeBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#keywordsCanBeId.
    def visitKeywordsCanBeId(self, ctx:mysqlParser.KeywordsCanBeIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mysqlParser#functionNameBase.
    def visitFunctionNameBase(self, ctx:mysqlParser.FunctionNameBaseContext):
        return self.visitChildren(ctx)



del mysqlParser