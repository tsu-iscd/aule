package com.ptsecurity.ktdbfw.generated.ast

import com.fasterxml.jackson.annotation.JsonProperty
import com.fasterxml.jackson.annotation.JsonSubTypes
import com.fasterxml.jackson.annotation.JsonTypeInfo
import com.fasterxml.jackson.annotation.JsonTypeName

enum class ActionOnObject(val value: String) {
    ADD("ADD"),
    DROP("DROP"),
    ;

    companion object {
        @JvmStatic
        private val map = ActionOnObject.values().associateBy(ActionOnObject::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown ActionOnObject value '$value'")
    }
}

enum class DataType(val value: String) {
    CHAR("CHAR"),
    VARCHAR("VARCHAR"),
    TINYTEXT("TINYTEXT"),
    TEXT("TEXT"),
    MEDIUMTEXT("MEDIUMTEXT"),
    LONGTEXT("LONGTEXT"),
    TINYINT("TINYINT"),
    SMALLINT("SMALLINT"),
    MEDIUMINT("MEDIUMINT"),
    INT("INT"),
    INTEGER("INTEGER"),
    BIGINT("BIGINT"),
    REAL("REAL"),
    DOUBLE("DOUBLE"),
    FLOAT("FLOAT"),
    DECIMAL("DECIMAL"),
    NUMERIC("NUMERIC"),
    DATE("DATE"),
    YEAR("YEAR"),
    TINYBLOB("TINYBLOB"),
    BLOB("BLOB"),
    MEDIUMBLOB("MEDIUMBLOB"),
    LONGBLOB("LONGBLOB"),
    BIT("BIT"),
    TIME("TIME"),
    TIMESTAMP("TIMESTAMP"),
    DATETIME("DATETIME"),
    BINARY("BINARY"),
    VARBINARY("VARBINARY"),
    ENUM("ENUM"),
    SET("SET"),
    ;

    companion object {
        @JvmStatic
        private val map = DataType.values().associateBy(DataType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown DataType value '$value'")
    }
}

enum class SpatialDataType(val value: String) {
    GEOMETRY("GEOMETRY"),
    POINT("POINT"),
    LINESTRING("LINESTRING"),
    POLYGON("POLYGON"),
    MULTIPOINT("MULTIPOINT"),
    MULTILINESTRING("MULTILINESTRING"),
    MULTIPOLYGON("MULTIPOLYGON"),
    GEOMETRYCOLLECTION("GEOMETRYCOLLECTION"),
    ;

    companion object {
        @JvmStatic
        private val map = SpatialDataType.values().associateBy(SpatialDataType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown SpatialDataType value '$value'")
    }
}

enum class ConvertedDataTypeValue(val value: String) {
    BINARY("BINARY"),
    NCHAR("NCHAR"),
    CHAR("CHAR"),
    DATE("DATE"),
    DATETIME("DATETIME"),
    TIME("TIME"),
    DECIMAL("DECIMAL"),
    SIGNED("SIGNED"),
    UNSIGNED("UNSIGNED"),
    ;

    companion object {
        @JvmStatic
        private val map = ConvertedDataTypeValue.values().associateBy(ConvertedDataTypeValue::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown ConvertedDataTypeValue value '$value'")
    }
}

enum class IntervalType(val value: String) {
    YEAR("YEAR"),
    YEAR_MONTH("YEAR_MONTH"),
    DAY_HOUR("DAY_HOUR"),
    DAY_MINUTE("DAY_MINUTE"),
    DAY_SECOND("DAY_SECOND"),
    HOUR_MINUTE("HOUR_MINUTE"),
    HOUR_SECOND("HOUR_SECOND"),
    MINUTE_SECOND("MINUTE_SECOND"),
    SECOND_MICROSECOND("SECOND_MICROSECOND"),
    MINUTE_MICROSECOND("MINUTE_MICROSECOND"),
    HOUR_MICROSECOND("HOUR_MICROSECOND"),
    DAY_MICROSECOND("DAY_MICROSECOND"),
    QUARTER("QUARTER"),
    MONTH("MONTH"),
    DAY("DAY"),
    HOUR("HOUR"),
    MINUTE("MINUTE"),
    WEEK("WEEK"),
    SECOND("SECOND"),
    MICROSECOND("MICROSECOND"),
    ;

    companion object {
        @JvmStatic
        private val map = IntervalType.values().associateBy(IntervalType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown IntervalType value '$value'")
    }
}

enum class LogicalOperator(val value: String) {
    OR("OR"),
    OR_SIGN("||"),
    XOR("XOR"),
    AND("AND"),
    AND_SIGN("&&"),
    NOT_SIGN("!"),
    NOT("NOT"),
    ;

    companion object {
        @JvmStatic
        private val map = LogicalOperator.values().associateBy(LogicalOperator::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown LogicalOperator value '$value'")
    }
}

enum class ComparisonOperator(val value: String) {
    EQ("="),
    GE(">="),
    GT(">"),
    LE("<="),
    LT("<"),
    NE("<>"),
    EMNE("!="),
    NSNE("<=>"),
    ;

    companion object {
        @JvmStatic
        private val map = ComparisonOperator.values().associateBy(ComparisonOperator::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown ComparisonOperator value '$value'")
    }
}

enum class UnaryOperator(val value: String) {
    BANG("!"),
    TILDE("~"),
    PLUS("+"),
    MINUS("-"),
    ;

    companion object {
        @JvmStatic
        private val map = UnaryOperator.values().associateBy(UnaryOperator::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown UnaryOperator value '$value'")
    }
}

enum class BinaryOperator(val value: String) {
    OR("|"),
    AND("&"),
    LSHIFT("<<"),
    RSHIFT(">>"),
    PLUS("+"),
    MINUS("-"),
    MULTIPLY("*"),
    DIVIDE("/"),
    MODULE("%"),
    DIV("DIV"),
    MOD("MOD"),
    XOR("^"),
    ;

    companion object {
        @JvmStatic
        private val map = BinaryOperator.values().associateBy(BinaryOperator::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown BinaryOperator value '$value'")
    }
}

enum class KeywordLiteral(val value: String) {
    DEFAULT("DEFAULT"),
    CURRENT_TIMESTAMP("CURRENT_TIMESTAMP"),
    MAXVALUE("MAXVALUE"),
    ;

    companion object {
        @JvmStatic
        private val map = KeywordLiteral.values().associateBy(KeywordLiteral::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown KeywordLiteral value '$value'")
    }
}

enum class RowAggregator(val value: String) {
    ALL("ALL"),
    DISTINCT("DISTINCT"),
    DISTINCTROW("DISTINCTROW"),
    ;

    companion object {
        @JvmStatic
        private val map = RowAggregator.values().associateBy(RowAggregator::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown RowAggregator value '$value'")
    }
}

enum class KeywordPosition(val value: String) {
    BEFORE("BEFORE"),
    AFTER("AFTER"),
    ;

    companion object {
        @JvmStatic
        private val map = KeywordPosition.values().associateBy(KeywordPosition::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown KeywordPosition value '$value'")
    }
}

enum class LogicalMatch(val value: String) {
    TRUE("TRUE"),
    FALSE("FALSE"),
    UNKNOWN("UNKNOWN"),
    ;

    companion object {
        @JvmStatic
        private val map = LogicalMatch.values().associateBy(LogicalMatch::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown LogicalMatch value '$value'")
    }
}

enum class QuantifierType(val value: String) {
    ALL("ALL"),
    ANY("ANY"),
    SOME("SOME"),
    ;

    companion object {
        @JvmStatic
        private val map = QuantifierType.values().associateBy(QuantifierType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown QuantifierType value '$value'")
    }
}

enum class TypeLike(val value: String) {
    SOUNDS("SOUNDS"),
    LIKE("LIKE"),
    RLIKE("RLIKE"),
    REGEXP("REGEXP"),
    ;

    companion object {
        @JvmStatic
        private val map = TypeLike.values().associateBy(TypeLike::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown TypeLike value '$value'")
    }
}

enum class StringTransformType(val value: String) {
    COLLATE("COLLATE"),
    BINARY("BINARY"),
    ;

    companion object {
        @JvmStatic
        private val map = StringTransformType.values().associateBy(StringTransformType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown StringTransformType value '$value'")
    }
}

enum class HandlerAction(val value: String) {
    CONTINUE("CONTINUE"),
    EXIT("EXIT"),
    UNDO("UNDO"),
    ;

    companion object {
        @JvmStatic
        private val map = HandlerAction.values().associateBy(HandlerAction::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown HandlerAction value '$value'")
    }
}

enum class CursorAction(val value: String) {
    OPEN("Open"),
    CLOSE("Close"),
    ;

    companion object {
        @JvmStatic
        private val map = CursorAction.values().associateBy(CursorAction::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown CursorAction value '$value'")
    }
}

enum class UnionType(val value: String) {
    ALL("ALL"),
    DISTINCT("DISTINCT"),
    ;

    companion object {
        @JvmStatic
        private val map = UnionType.values().associateBy(UnionType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown UnionType value '$value'")
    }
}

enum class SortType(val value: String) {
    ASC("ASC"),
    DESC("DESC"),
    ;

    companion object {
        @JvmStatic
        private val map = SortType.values().associateBy(SortType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown SortType value '$value'")
    }
}

enum class JoinType(val value: String) {
    INNERJOIN("INNERJOIN"),
    CROSSJOIN("CROSSJOIN"),
    STRAIGHTJOIN("STRAIGHTJOIN"),
    LEFTJOIN("LEFTJOIN"),
    LEFTOUTERJOIN("LEFTOUTERJOIN"),
    RIGHTJOIN("RIGHTJOIN"),
    RIGHTOUTERJOIN("RIGHTOUTERJOIN"),
    FULLJOIN("FULLJOIN"),
    FULLOUTERJOIN("FULLOUTERJOIN"),
    NATURALJOIN("NATURALJOIN"),
    NATURALLEFTJOIN("NATURALLEFTJOIN"),
    NATURALLEFTOUTERJOIN("NATURALLEFTOUTERJOIN"),
    NATURALRIGHTJOIN("NATURALRIGHTJOIN"),
    NATURALRIGHTOUTERJOIN("NATURALRIGHTOUTERJOIN"),
    ;

    companion object {
        @JvmStatic
        private val map = JoinType.values().associateBy(JoinType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown JoinType value '$value'")
    }
}

enum class IndexHintAction(val value: String) {
    USE("USE"),
    IGNORE("IGNORE"),
    FORCE("FORCE"),
    ;

    companion object {
        @JvmStatic
        private val map = IndexHintAction.values().associateBy(IndexHintAction::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown IndexHintAction value '$value'")
    }
}

enum class IndexType(val value: String) {
    BTREE("BTREE"),
    HASH("HASH"),
    ;

    companion object {
        @JvmStatic
        private val map = IndexType.values().associateBy(IndexType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown IndexType value '$value'")
    }
}

enum class IndexHintType(val value: String) {
    JOIN("JOIN"),
    ORDERBY("ORDERBY"),
    GROUPBY("GROUPBY"),
    ;

    companion object {
        @JvmStatic
        private val map = IndexHintType.values().associateBy(IndexHintType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown IndexHintType value '$value'")
    }
}

enum class SimpleGroupByOperatorType(val value: String) {
    ROLLUP("ROLLUP"),
    CUBE("CUBE"),
    ;

    companion object {
        @JvmStatic
        private val map = SimpleGroupByOperatorType.values().associateBy(SimpleGroupByOperatorType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown SimpleGroupByOperatorType value '$value'")
    }
}

enum class Priority(val value: String) {
    LOWPRIORITY("LOWPRIORITY"),
    DELAYED("DELAYED"),
    HIGHPRIORITY("HIGHPRIORITY"),
    ;

    companion object {
        @JvmStatic
        private val map = Priority.values().associateBy(Priority::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown Priority value '$value'")
    }
}

enum class ColumnFormat(val value: String) {
    FIXED("FIXED"),
    DYNAMIC("DYNAMIC"),
    DEFAULT("DEFAULT"),
    ;

    companion object {
        @JvmStatic
        private val map = ColumnFormat.values().associateBy(ColumnFormat::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown ColumnFormat value '$value'")
    }
}

enum class ColumnStorage(val value: String) {
    DISK("DISK"),
    MEMORY("MEMORY"),
    DEFAULT("DEFAULT"),
    ;

    companion object {
        @JvmStatic
        private val map = ColumnStorage.values().associateBy(ColumnStorage::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown ColumnStorage value '$value'")
    }
}

enum class ForeignKeyMatchType(val value: String) {
    FULL("FULL"),
    PARTIAL("PARTIAL"),
    SIMPLE("SIMPLE"),
    ;

    companion object {
        @JvmStatic
        private val map = ForeignKeyMatchType.values().associateBy(ForeignKeyMatchType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown ForeignKeyMatchType value '$value'")
    }
}

enum class ReferenceConstraintType(val value: String) {
    RESTRICT("RESTRICT"),
    CASCADE("CASCADE"),
    SETNULL("SETNULL"),
    NOACTION("NOACTION"),
    SETDEFAULT("SETDEFAULT"),
    ;

    companion object {
        @JvmStatic
        private val map = ReferenceConstraintType.values().associateBy(ReferenceConstraintType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown ReferenceConstraintType value '$value'")
    }
}

enum class KeyType(val value: String) {
    PRIMARY("PRIMARY"),
    UNIQUE("UNIQUE"),
    FOREIGN("FOREIGN"),
    INDEX("INDEX"),
    KEY("KEY"),
    FULLTEXT("FULLTEXT"),
    SPATIAL("SPATIAL"),
    ;

    companion object {
        @JvmStatic
        private val map = KeyType.values().associateBy(KeyType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown KeyType value '$value'")
    }
}

enum class CompressionTableType(val value: String) {
    ZLIB("ZLIB"),
    LZ4("LZ4"),
    NONE("NONE"),
    ;

    companion object {
        @JvmStatic
        private val map = CompressionTableType.values().associateBy(CompressionTableType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown CompressionTableType value '$value'")
    }
}

enum class SelectSpecificators(val value: String) {
    ALL("ALL"),
    DISTINCT("DISTINCT"),
    DISTINCTROW("DISTINCTROW"),
    HIGHPRIORITY("HIGHPRIORITY"),
    STRAIGHTJOIN("STRAIGHTJOIN"),
    SQLSMALLRESULT("SQLSMALLRESULT"),
    SQLBIGRESULT("SQLBIGRESULT"),
    SQLBUFFERRESULT("SQLBUFFERRESULT"),
    SQLCACHE("SQLCACHE"),
    SQLNOCACHE("SQLNOCACHE"),
    SQLCALCFOUNDROWS("SQLCALCFOUNDROWS"),
    ;

    companion object {
        @JvmStatic
        private val map = SelectSpecificators.values().associateBy(SelectSpecificators::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown SelectSpecificators value '$value'")
    }
}

enum class InsertViolateBehaviour(val value: String) {
    IGNORE("IGNORE"),
    REPLACE("REPLACE"),
    ;

    companion object {
        @JvmStatic
        private val map = InsertViolateBehaviour.values().associateBy(InsertViolateBehaviour::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown InsertViolateBehaviour value '$value'")
    }
}

enum class InsertTableMethod(val value: String) {
    NO("NO"),
    FIRST("FIRST"),
    LAST("LAST"),
    ;

    companion object {
        @JvmStatic
        private val map = InsertTableMethod.values().associateBy(InsertTableMethod::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown InsertTableMethod value '$value'")
    }
}

enum class TableKeyPacking(val value: String) {
    YES("YES"),
    NO("NO"),
    DEFAULT("DEFAULT"),
    ;

    companion object {
        @JvmStatic
        private val map = TableKeyPacking.values().associateBy(TableKeyPacking::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown TableKeyPacking value '$value'")
    }
}

enum class FormatTableRow(val value: String) {
    DEFAULT("DEFAULT"),
    DYNAMIC("DYNAMIC"),
    FIXED("FIXED"),
    COMPRESSED("COMPRESSED"),
    REDUNDANT("REDUNDANT"),
    COMPACT("COMPACT"),
    ;

    companion object {
        @JvmStatic
        private val map = FormatTableRow.values().associateBy(FormatTableRow::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown FormatTableRow value '$value'")
    }
}

enum class StatisticsTableType(val value: String) {
    YES("YES"),
    NO("NO"),
    DEFAULT("DEFAULT"),
    ;

    companion object {
        @JvmStatic
        private val map = StatisticsTableType.values().associateBy(StatisticsTableType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown StatisticsTableType value '$value'")
    }
}

enum class TablespaceStorage(val value: String) {
    DISK("DISK"),
    MEMORY("MEMORY"),
    DEFAULT("DEFAULT"),
    ;

    companion object {
        @JvmStatic
        private val map = TablespaceStorage.values().associateBy(TablespaceStorage::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown TablespaceStorage value '$value'")
    }
}

enum class DeletionFormat(val value: String) {
    USING("USING"),
    FROM("FROM"),
    ;

    companion object {
        @JvmStatic
        private val map = DeletionFormat.values().associateBy(DeletionFormat::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown DeletionFormat value '$value'")
    }
}

enum class IndexCategory(val value: String) {
    UNIQUE("UNIQUE"),
    FULLTEXT("FULLTEXT"),
    SPATIAL("SPATIAL"),
    ;

    companion object {
        @JvmStatic
        private val map = IndexCategory.values().associateBy(IndexCategory::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown IndexCategory value '$value'")
    }
}

enum class IndexAlgorithmOption(val value: String) {
    DEFAULT("DEFAULT"),
    INPLACE("INPLACE"),
    COPY("COPY"),
    ;

    companion object {
        @JvmStatic
        private val map = IndexAlgorithmOption.values().associateBy(IndexAlgorithmOption::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown IndexAlgorithmOption value '$value'")
    }
}

enum class LockOption(val value: String) {
    DEFAULT("DEFAULT"),
    NONE("NONE"),
    SHARED("SHARED"),
    EXCLUSIVE("EXCLUSIVE"),
    ;

    companion object {
        @JvmStatic
        private val map = LockOption.values().associateBy(LockOption::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown LockOption value '$value'")
    }
}

enum class RoutineOperator(val value: String) {
    CONTAINSSQL("CONTAINSSQL"),
    NOSQL("NOSQL"),
    READSSQLDATA("READSSQLDATA"),
    MODIFIESSQLDATA("MODIFIESSQLDATA"),
    ;

    companion object {
        @JvmStatic
        private val map = RoutineOperator.values().associateBy(RoutineOperator::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown RoutineOperator value '$value'")
    }
}

enum class SecurityOwnerContext(val value: String) {
    DEFINER("DEFINER"),
    INVOKER("INVOKER"),
    ;

    companion object {
        @JvmStatic
        private val map = SecurityOwnerContext.values().associateBy(SecurityOwnerContext::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown SecurityOwnerContext value '$value'")
    }
}

enum class LiteralUserName(val value: String) {
    CURRENTUSER("CURRENTUSER"),
    ;

    companion object {
        @JvmStatic
        private val map = LiteralUserName.values().associateBy(LiteralUserName::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown LiteralUserName value '$value'")
    }
}

enum class ParameterDirection(val value: String) {
    IN("IN"),
    OUT("OUT"),
    INOUT("INOUT"),
    ;

    companion object {
        @JvmStatic
        private val map = ParameterDirection.values().associateBy(ParameterDirection::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown ParameterDirection value '$value'")
    }
}

enum class AlgorithmView(val value: String) {
    UNDEFINED("UNDEFINED"),
    MERGE("MERGE"),
    TEMPTABLE("TEMPTABLE"),
    ;

    companion object {
        @JvmStatic
        private val map = AlgorithmView.values().associateBy(AlgorithmView::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown AlgorithmView value '$value'")
    }
}

enum class CheckOptionView(val value: String) {
    CASCADED("CASCADED"),
    LOCAL("LOCAL"),
    EMPTY(""),
    ;

    companion object {
        @JvmStatic
        private val map = CheckOptionView.values().associateBy(CheckOptionView::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown CheckOptionView value '$value'")
    }
}

enum class TimeTrigger(val value: String) {
    BEFORE("BEFORE"),
    AFTER("AFTER"),
    ;

    companion object {
        @JvmStatic
        private val map = TimeTrigger.values().associateBy(TimeTrigger::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown TimeTrigger value '$value'")
    }
}

enum class EventTrigger(val value: String) {
    INSERT("INSERT"),
    UPDATE("UPDATE"),
    DELETE("DELETE"),
    ;

    companion object {
        @JvmStatic
        private val map = EventTrigger.values().associateBy(EventTrigger::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown EventTrigger value '$value'")
    }
}

enum class OrderTriggerType(val value: String) {
    FOLLOWS("FOLLOWS"),
    PRECEDES("PRECEDES"),
    ;

    companion object {
        @JvmStatic
        private val map = OrderTriggerType.values().associateBy(OrderTriggerType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown OrderTriggerType value '$value'")
    }
}

enum class EnableEventType(val value: String) {
    ENABLE("ENABLE"),
    DISABLE("DISABLE"),
    DISABLEONSLAVE("DISABLEONSLAVE"),
    ;

    companion object {
        @JvmStatic
        private val map = EnableEventType.values().associateBy(EnableEventType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown EnableEventType value '$value'")
    }
}

enum class IntimeActionType(val value: String) {
    ONLINE("ONLINE"),
    OFFLINE("OFFLINE"),
    ;

    companion object {
        @JvmStatic
        private val map = IntimeActionType.values().associateBy(IntimeActionType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown IntimeActionType value '$value'")
    }
}

enum class PartitionAction(val value: String) {
    ADD("ADD"),
    DROP("DROP"),
    DISCARD("DISCARD"),
    IMPORT("IMPORT"),
    TRUNCATE("TRUNCATE"),
    COALESCE("COALESCE"),
    REORGANIZE("REORGANIZE"),
    EXCHANGE("EXCHANGE"),
    ANALYZE("ANALYZE"),
    CHECK("CHECK"),
    OPTIMIZE("OPTIMIZE"),
    REBUILD("REBUILD"),
    REPAIR("REPAIR"),
    ;

    companion object {
        @JvmStatic
        private val map = PartitionAction.values().associateBy(PartitionAction::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown PartitionAction value '$value'")
    }
}

enum class AlterAction(val value: String) {
    ALGORITHM("ALGORITHM"),
    LOCK("LOCK"),
    DISABLEKEYS("DISABLEKEYS"),
    ENABLEKEYS("ENABLEKEYS"),
    RENAME("RENAME"),
    ORDERBY("ORDERBY"),
    CONVERTCHARSET("CONVERTCHARSET"),
    DEFAULTCHARSET("DEFAULTCHARSET"),
    DISCARDTABLESPACE("DISCARDTABLESPACE"),
    IMPORTTABLESPACE("IMPORTTABLESPACE"),
    FORCE("FORCE"),
    VALIDATION("VALIDATION"),
    REMOVEPARTITIONING("REMOVEPARTITIONING"),
    UPGRADEPARTITIONING("UPGRADEPARTITIONING"),
    ;

    companion object {
        @JvmStatic
        private val map = AlterAction.values().associateBy(AlterAction::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown AlterAction value '$value'")
    }
}

enum class ConstraintDropType(val value: String) {
    RESTRICT("RESTRICT"),
    CASCADE("CASCADE"),
    ;

    companion object {
        @JvmStatic
        private val map = ConstraintDropType.values().associateBy(ConstraintDropType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown ConstraintDropType value '$value'")
    }
}

enum class IndexOrder(val value: String) {
    FIRST("FIRST"),
    NEXT("NEXT"),
    PREV("PREV"),
    LAST("LAST"),
    ;

    companion object {
        @JvmStatic
        private val map = IndexOrder.values().associateBy(IndexOrder::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown IndexOrder value '$value'")
    }
}

enum class TransactionOption(val value: String) {
    WITHCONSISTENTSNAPSHOT("WITHCONSISTENTSNAPSHOT"),
    READWRITE("READWRITE"),
    READONLY("READONLY"),
    ;

    companion object {
        @JvmStatic
        private val map = TransactionOption.values().associateBy(TransactionOption::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown TransactionOption value '$value'")
    }
}

enum class TransactionContext(val value: String) {
    GLOBAL("GLOBAL"),
    SESSION("SESSION"),
    ;

    companion object {
        @JvmStatic
        private val map = TransactionContext.values().associateBy(TransactionContext::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown TransactionContext value '$value'")
    }
}

enum class TransactionLevel(val value: String) {
    REPEATABLEREAD("REPEATABLEREAD"),
    READCOMMITTED("READCOMMITTED"),
    READUNCOMMITTED("READUNCOMMITTED"),
    SERIALIZABLE("SERIALIZABLE"),
    ;

    companion object {
        @JvmStatic
        private val map = TransactionLevel.values().associateBy(TransactionLevel::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown TransactionLevel value '$value'")
    }
}

enum class ThreadType(val value: String) {
    IOTHREAD("IOTHREAD"),
    SQLTHREAD("SQLTHREAD"),
    ;

    companion object {
        @JvmStatic
        private val map = ThreadType.values().associateBy(ThreadType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown ThreadType value '$value'")
    }
}

enum class TLSOptionName(val value: String) {
    SSL("SSL"),
    X509("X509"),
    CIPHER("CIPHER"),
    ISSUER("ISSUER"),
    SUBJECT("SUBJECT"),
    ;

    companion object {
        @JvmStatic
        private val map = TLSOptionName.values().associateBy(TLSOptionName::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown TLSOptionName value '$value'")
    }
}

enum class UserResourceType(val value: String) {
    QUERIESPERHOUR("QUERIESPERHOUR"),
    UPDATEPERHOUR("UPDATEPERHOUR"),
    CONNECTIONSPERHOUR("CONNECTIONSPERHOUR"),
    USERCONNECTIONS("USERCONNECTIONS"),
    ;

    companion object {
        @JvmStatic
        private val map = UserResourceType.values().associateBy(UserResourceType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown UserResourceType value '$value'")
    }
}

enum class PasswordExpirationType(val value: String) {
    DEFAULT("DEFAULT"),
    NEVER("NEVER"),
    INTERVAL("INTERVAL"),
    ;

    companion object {
        @JvmStatic
        private val map = PasswordExpirationType.values().associateBy(PasswordExpirationType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown PasswordExpirationType value '$value'")
    }
}

enum class PrivilegeName(val value: String) {
    ALL("ALL"),
    ALLPRIVILEGES("ALLPRIVILEGES"),
    ALTER("ALTER"),
    ALTERROUTINE("ALTERROUTINE"),
    CREATE("CREATE"),
    CREATETEMPORARYTABLES("CREATETEMPORARYTABLES"),
    CREATEROUTINE("CREATEROUTINE"),
    CREATEVIEW("CREATEVIEW"),
    CREATEUSER("CREATEUSER"),
    CREATETABLESPACE("CREATETABLESPACE"),
    DELETE("DELETE"),
    DROP("DROP"),
    EVENT("EVENT"),
    EXECUTE("EXECUTE"),
    FILE("FILE"),
    GRANTOPTION("GRANTOPTION"),
    INDEX("INDEX"),
    INSERT("INSERT"),
    LOCKTABLES("LOCKTABLES"),
    PROCESS("PROCESS"),
    PROXY("PROXY"),
    REFERENCES("REFERENCES"),
    RELOAD("RELOAD"),
    REPLICATIONCLIENT("REPLICATIONCLIENT"),
    REPLICATIONSLAVE("REPLICATIONSLAVE"),
    SELECT("SELECT"),
    SHOWVIEW("SHOWVIEW"),
    SHOWDATABASES("SHOWDATABASES"),
    SHUTDOWN("SHUTDOWN"),
    SUPER("SUPER"),
    TRIGGER("TRIGGER"),
    UPDATE("UPDATE"),
    USAGE("USAGE"),
    ;

    companion object {
        @JvmStatic
        private val map = PrivilegeName.values().associateBy(PrivilegeName::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown PrivilegeName value '$value'")
    }
}

enum class PrivilegeLevel(val value: String) {
    GLOBAL("GLOBAL"),
    SCHEMA("SCHEMA"),
    TABLE("TABLE"),
    ROUTINE("ROUTINE"),
    ;

    companion object {
        @JvmStatic
        private val map = PrivilegeLevel.values().associateBy(PrivilegeLevel::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown PrivilegeLevel value '$value'")
    }
}

enum class PrivilegeObjectType(val value: String) {
    TABLE("TABLE"),
    FUNCTION("FUNCTION"),
    PROCEDURE("PROCEDURE"),
    ;

    companion object {
        @JvmStatic
        private val map = PrivilegeObjectType.values().associateBy(PrivilegeObjectType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown PrivilegeObjectType value '$value'")
    }
}

enum class LockTableAction(val value: String) {
    READ("READ"),
    READLOCAL("READLOCAL"),
    WRITE("WRITE"),
    LOWPRIORITYWRITE("LOWPRIORITYWRITE"),
    ;

    companion object {
        @JvmStatic
        private val map = LockTableAction.values().associateBy(LockTableAction::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown LockTableAction value '$value'")
    }
}

enum class CheckTableOption(val value: String) {
    FORUPGRADE("FORUPGRADE"),
    QUICK("QUICK"),
    FAST("FAST"),
    MEDIUM("MEDIUM"),
    EXTENDED("EXTENDED"),
    CHANGED("CHANGED"),
    ;

    companion object {
        @JvmStatic
        private val map = CheckTableOption.values().associateBy(CheckTableOption::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown CheckTableOption value '$value'")
    }
}

enum class ReturnDataType(val value: String) {
    STRING("STRING"),
    INTEGER("INTEGER"),
    REAL("REAL"),
    DECIMAL("DECIMAL"),
    ;

    companion object {
        @JvmStatic
        private val map = ReturnDataType.values().associateBy(ReturnDataType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown ReturnDataType value '$value'")
    }
}

enum class ProfileType(val value: String) {
    ALL("ALL"),
    BLOCKIO("BLOCKIO"),
    CONTEXTSWITCHES("CONTEXTSWITCHES"),
    CPU("CPU"),
    IPC("IPC"),
    MEMORY("MEMORY"),
    PAGEFAULTS("PAGEFAULTS"),
    SOURCE("SOURCE"),
    SWAPS("SWAPS"),
    ;

    companion object {
        @JvmStatic
        private val map = ProfileType.values().associateBy(ProfileType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown ProfileType value '$value'")
    }
}

enum class FlushOption(val value: String) {
    DESKEYFILE("DESKEYFILE"),
    HOSTS("HOSTS"),
    BINARYLOGS("BINARYLOGS"),
    ENGINELOGS("ENGINELOGS"),
    ERRORLOGS("ERRORLOGS"),
    CENERALLOGS("CENERALLOGS"),
    RELAYLOGS("RELAYLOGS"),
    SLOWLOGS("SLOWLOGS"),
    LOGS("LOGS"),
    OPTIMIZERCOSTS("OPTIMIZERCOSTS"),
    PRIVILEGES("PRIVILEGES"),
    QUERYCACHE("QUERYCACHE"),
    STATUS("STATUS"),
    USERRESOURCES("USERRESOURCES"),
    TABLES("TABLES"),
    TABLESWITHREADLOCK("TABLESWITHREADLOCK"),
    ;

    companion object {
        @JvmStatic
        private val map = FlushOption.values().associateBy(FlushOption::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown FlushOption value '$value'")
    }
}

enum class DescriptionStatementType(val value: String) {
    DESC("DESC"),
    DESCRIBE("DESCRIBE"),
    EXPLAIN("EXPLAIN"),
    ;

    companion object {
        @JvmStatic
        private val map = DescriptionStatementType.values().associateBy(DescriptionStatementType::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown DescriptionStatementType value '$value'")
    }
}

enum class FormatDescriptionObject(val value: String) {
    EXTENDED("EXTENDED"),
    PARTITIONS("PARTITIONS"),
    FORMAT("FORMAT"),
    ;

    companion object {
        @JvmStatic
        private val map = FormatDescriptionObject.values().associateBy(FormatDescriptionObject::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown FormatDescriptionObject value '$value'")
    }
}

enum class DescribeFormatValue(val value: String) {
    TRADITIONAL("TRADITIONAL"),
    JSON("JSON"),
    ;

    companion object {
        @JvmStatic
        private val map = DescribeFormatValue.values().associateBy(DescribeFormatValue::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown DescribeFormatValue value '$value'")
    }
}

enum class SyntaxFormat(val value: String) {
    COLUMNS("COLUMNS"),
    FIELDS("FIELDS"),
    FROM("FROM"),
    IN("IN"),
    GLOBAL("GLOBAL"),
    SESSION("SESSION"),
    DATABASE("DATABASE"),
    SCHEMA("SCHEMA"),
    AS("AS"),
    INDEX("INDEX"),
    KEY("KEY"),
    CHARACTERSET("CHARACTERSET"),
    CHARSET("CHARSET"),
    WITH("WITH"),
    WITHOUT("WITHOUT"),
    TO("TO"),
    LINES("LINES"),
    ROWS("ROWS"),
    FORUPDATE("FORUPDATE"),
    LOCKINSHAREMODE("LOCKINSHAREMODE"),
    BINARY("BINARY"),
    MASTER("MASTER"),
    START("START"),
    BEGIN("BEGIN"),
    JOIN("JOIN"),
    RESUME("RESUME"),
    SUSPEND("SUSPEND"),
    SUSPENDFORMIGRATE("SUSPENDFORMIGRATE"),
    ONEPHASE("ONEPHASE"),
    DROP("DROP"),
    DEALLOCATE("DEALLOCATE"),
    BY("BY"),
    BYPASSWORD("BYPASSWORD"),
    RELAYLOG("RELAYLOG"),
    STATUS("STATUS"),
    MUTEX("MUTEX"),
    CONNECTION("CONNECTION"),
    QUERY("QUERY"),
    PASSWORD("PASSWORD"),
    OLDPASSWORD("OLDPASSWORD"),
    ;

    companion object {
        @JvmStatic
        private val map = SyntaxFormat.values().associateBy(SyntaxFormat::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown SyntaxFormat value '$value'")
    }
}

enum class NamedEntity(val value: String) {
    PROCEDURE("PROCEDURE"),
    EVENT("EVENT"),
    FUNCTION("FUNCTION"),
    TABLE("TABLE"),
    TRIGGER("TRIGGER"),
    VIEW("VIEW"),
    ;

    companion object {
        @JvmStatic
        private val map = NamedEntity.values().associateBy(NamedEntity::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown NamedEntity value '$value'")
    }
}

enum class CommonEntity(val value: String) {
    CHARACTERSET("CHARACTERSET"),
    COLLATION("COLLATION"),
    DATABASES("DATABASES"),
    SCHEMAS("SCHEMAS"),
    FUNCTIONSTATUS("FUNCTIONSTATUS"),
    PROCEDURESTATUS("PROCEDURESTATUS"),
    STATUS("STATUS"),
    VARIABLES("VARIABLES"),
    GLOBALSTATUS("GLOBALSTATUS"),
    GLOBALVARIABLES("GLOBALVARIABLES"),
    SESSIONSTATUS("SESSIONSTATUS"),
    SESSIONVARIABLES("SESSIONVARIABLES"),
    STORAGEENGINES("STORAGEENGINES"),
    ENGINES("ENGINES"),
    MASTERSTATUS("MASTERSTATUS"),
    PLUGINS("PLUGINS"),
    PRIVILEGES("PRIVILEGES"),
    FULLPROCESSLIST("FULLPROCESSLIST"),
    PROCESSLIST("PROCESSLIST"),
    PROFILES("PROFILES"),
    SLAVEHOSTS("SLAVEHOSTS"),
    AUTHORS("AUTHORS"),
    CONTRIBUTORS("CONTRIBUTORS"),
    ERRORS("ERRORS"),
    WARNINGS("WARNINGS"),
    EVENTS("EVENTS"),
    TABLESTATUS("TABLESTATUS"),
    FULLTABLES("FULLTABLES"),
    TABLES("TABLES"),
    TRIGGERS("TRIGGERS"),
    KEYS("KEYS"),
    INDEX("INDEX"),
    INDEXES("INDEXES"),
    ;

    companion object {
        @JvmStatic
        private val map = CommonEntity.values().associateBy(CommonEntity::value);
        @JvmStatic
        fun fromValue(value: String?) = map[value?.toUpperCase()]
                                        ?: throw IllegalArgumentException("Unknown CommonEntity value '$value'")
    }
}


@JsonTypeInfo(
    use = JsonTypeInfo.Id.NAME,
    include = JsonTypeInfo.As.PROPERTY,
    property = "type")
@JsonSubTypes(
    JsonSubTypes.Type(value = Node::class, name = "Node"),
    JsonSubTypes.Type(value = Script::class, name = "Script"),
    JsonSubTypes.Type(value = CommonStatement::class, name = "CommonStatement"),
    JsonSubTypes.Type(value = Statement::class, name = "Statement"),
    JsonSubTypes.Type(value = SingleQueryStatement::class, name = "SingleQueryStatement"),
    JsonSubTypes.Type(value = EmptyStatement::class, name = "EmptyStatement"),
    JsonSubTypes.Type(value = WithStatement::class, name = "WithStatement"),
    JsonSubTypes.Type(value = CreateDatabaseStatement::class, name = "CreateDatabaseStatement"),
    JsonSubTypes.Type(value = CreateEventStatement::class, name = "CreateEventStatement"),
    JsonSubTypes.Type(value = CreateIndexStatement::class, name = "CreateIndexStatement"),
    JsonSubTypes.Type(value = CreateLogFileGroupStatement::class, name = "CreateLogFileGroupStatement"),
    JsonSubTypes.Type(value = CreateProcedureStatement::class, name = "CreateProcedureStatement"),
    JsonSubTypes.Type(value = CreateFunctionStatement::class, name = "CreateFunctionStatement"),
    JsonSubTypes.Type(value = CreateServerStatement::class, name = "CreateServerStatement"),
    JsonSubTypes.Type(value = CreateTableStatement::class, name = "CreateTableStatement"),
    JsonSubTypes.Type(value = CopyCreateTableStatement::class, name = "CopyCreateTableStatement"),
    JsonSubTypes.Type(value = QueryCreateTableStatement::class, name = "QueryCreateTableStatement"),
    JsonSubTypes.Type(value = ColumnCreateTableStatement::class, name = "ColumnCreateTableStatement"),
    JsonSubTypes.Type(value = CreateTableSpaceStatement::class, name = "CreateTableSpaceStatement"),
    JsonSubTypes.Type(value = CreateTriggerStatement::class, name = "CreateTriggerStatement"),
    JsonSubTypes.Type(value = TriggerOrderClause::class, name = "TriggerOrderClause"),
    JsonSubTypes.Type(value = CreateViewStatement::class, name = "CreateViewStatement"),
    JsonSubTypes.Type(value = EventScheduleClause::class, name = "EventScheduleClause"),
    JsonSubTypes.Type(value = EventSchedulePresicion::class, name = "EventSchedulePresicion"),
    JsonSubTypes.Type(value = EventScheduleInterval::class, name = "EventScheduleInterval"),
    JsonSubTypes.Type(value = RoutineParameter::class, name = "RoutineParameter"),
    JsonSubTypes.Type(value = ColumnDeclaration::class, name = "ColumnDeclaration"),
    JsonSubTypes.Type(value = ConstraintDeclaration::class, name = "ConstraintDeclaration"),
    JsonSubTypes.Type(value = ConstraintKeyClause::class, name = "ConstraintKeyClause"),
    JsonSubTypes.Type(value = ConstraintCheckClause::class, name = "ConstraintCheckClause"),
    JsonSubTypes.Type(value = ReferenceDeclarationClause::class, name = "ReferenceDeclarationClause"),
    JsonSubTypes.Type(value = PartitionClause::class, name = "PartitionClause"),
    JsonSubTypes.Type(value = PartitionFunction::class, name = "PartitionFunction"),
    JsonSubTypes.Type(value = PartitionHash::class, name = "PartitionHash"),
    JsonSubTypes.Type(value = PartitionKey::class, name = "PartitionKey"),
    JsonSubTypes.Type(value = PartitionRange::class, name = "PartitionRange"),
    JsonSubTypes.Type(value = PartitionList::class, name = "PartitionList"),
    JsonSubTypes.Type(value = SubPartitionFunction::class, name = "SubPartitionFunction"),
    JsonSubTypes.Type(value = SubPartitionHash::class, name = "SubPartitionHash"),
    JsonSubTypes.Type(value = SubPartitionKey::class, name = "SubPartitionKey"),
    JsonSubTypes.Type(value = PartitionDefinition::class, name = "PartitionDefinition"),
    JsonSubTypes.Type(value = ComparasionPartitionDefinition::class, name = "ComparasionPartitionDefinition"),
    JsonSubTypes.Type(value = ListPartitionDefinition::class, name = "ListPartitionDefinition"),
    JsonSubTypes.Type(value = SimplePartitionDefinition::class, name = "SimplePartitionDefinition"),
    JsonSubTypes.Type(value = SubPartitionDefinition::class, name = "SubPartitionDefinition"),
    JsonSubTypes.Type(value = AlterDatabaseStatement::class, name = "AlterDatabaseStatement"),
    JsonSubTypes.Type(value = AlterEventStatement::class, name = "AlterEventStatement"),
    JsonSubTypes.Type(value = AlterFunctionStatement::class, name = "AlterFunctionStatement"),
    JsonSubTypes.Type(value = AlterInstanceStatement::class, name = "AlterInstanceStatement"),
    JsonSubTypes.Type(value = AlterLogFileGroupStatement::class, name = "AlterLogFileGroupStatement"),
    JsonSubTypes.Type(value = AlterProcedureStatement::class, name = "AlterProcedureStatement"),
    JsonSubTypes.Type(value = AlterServerStatement::class, name = "AlterServerStatement"),
    JsonSubTypes.Type(value = AlterTableStatement::class, name = "AlterTableStatement"),
    JsonSubTypes.Type(value = AlterTableSpaceStatement::class, name = "AlterTableSpaceStatement"),
    JsonSubTypes.Type(value = AlterViewStatement::class, name = "AlterViewStatement"),
    JsonSubTypes.Type(value = AlterSpecification::class, name = "AlterSpecification"),
    JsonSubTypes.Type(value = AlterTableOption::class, name = "AlterTableOption"),
    JsonSubTypes.Type(value = AlterAddColumn::class, name = "AlterAddColumn"),
    JsonSubTypes.Type(value = AlterAddColumns::class, name = "AlterAddColumns"),
    JsonSubTypes.Type(value = AlterSetDefaultColumn::class, name = "AlterSetDefaultColumn"),
    JsonSubTypes.Type(value = AlterDropDefaultColumn::class, name = "AlterDropDefaultColumn"),
    JsonSubTypes.Type(value = AlterChangeColumn::class, name = "AlterChangeColumn"),
    JsonSubTypes.Type(value = AlterModifyColumn::class, name = "AlterModifyColumn"),
    JsonSubTypes.Type(value = AlterDropColumn::class, name = "AlterDropColumn"),
    JsonSubTypes.Type(value = AlterAddKey::class, name = "AlterAddKey"),
    JsonSubTypes.Type(value = AlterDropKey::class, name = "AlterDropKey"),
    JsonSubTypes.Type(value = AlterSpecPartition::class, name = "AlterSpecPartition"),
    JsonSubTypes.Type(value = AlterSpecCommon::class, name = "AlterSpecCommon"),
    JsonSubTypes.Type(value = DropDatabaseStatement::class, name = "DropDatabaseStatement"),
    JsonSubTypes.Type(value = DropEventStatement::class, name = "DropEventStatement"),
    JsonSubTypes.Type(value = DropIndexStatement::class, name = "DropIndexStatement"),
    JsonSubTypes.Type(value = DropLogfileGroupStatement::class, name = "DropLogfileGroupStatement"),
    JsonSubTypes.Type(value = DropProcedureStatement::class, name = "DropProcedureStatement"),
    JsonSubTypes.Type(value = DropFunctionStatement::class, name = "DropFunctionStatement"),
    JsonSubTypes.Type(value = DropServerStatement::class, name = "DropServerStatement"),
    JsonSubTypes.Type(value = DropTableStatement::class, name = "DropTableStatement"),
    JsonSubTypes.Type(value = DropTablespaceStatement::class, name = "DropTablespaceStatement"),
    JsonSubTypes.Type(value = DropTriggerStatement::class, name = "DropTriggerStatement"),
    JsonSubTypes.Type(value = DropViewStatement::class, name = "DropViewStatement"),
    JsonSubTypes.Type(value = RenameStatement::class, name = "RenameStatement"),
    JsonSubTypes.Type(value = RenameTableClause::class, name = "RenameTableClause"),
    JsonSubTypes.Type(value = TruncateStatement::class, name = "TruncateStatement"),
    JsonSubTypes.Type(value = CallStatement::class, name = "CallStatement"),
    JsonSubTypes.Type(value = DeleteStatement::class, name = "DeleteStatement"),
    JsonSubTypes.Type(value = SingleDeleteStatement::class, name = "SingleDeleteStatement"),
    JsonSubTypes.Type(value = MultipleDeleteStatement::class, name = "MultipleDeleteStatement"),
    JsonSubTypes.Type(value = DoStatement::class, name = "DoStatement"),
    JsonSubTypes.Type(value = HandlerStatement::class, name = "HandlerStatement"),
    JsonSubTypes.Type(value = HandlerOpenStatement::class, name = "HandlerOpenStatement"),
    JsonSubTypes.Type(value = HandlerReadComparasionStatement::class, name = "HandlerReadComparasionStatement"),
    JsonSubTypes.Type(value = HandlerReadOrderedStatement::class, name = "HandlerReadOrderedStatement"),
    JsonSubTypes.Type(value = HandlerReadSimpleStatement::class, name = "HandlerReadSimpleStatement"),
    JsonSubTypes.Type(value = HandlerCloseStatement::class, name = "HandlerCloseStatement"),
    JsonSubTypes.Type(value = InsertStatement::class, name = "InsertStatement"),
    JsonSubTypes.Type(value = InsertSetStatement::class, name = "InsertSetStatement"),
    JsonSubTypes.Type(value = InsertQueryStatement::class, name = "InsertQueryStatement"),
    JsonSubTypes.Type(value = InsertRowStatement::class, name = "InsertRowStatement"),
    JsonSubTypes.Type(value = InsertRowClause::class, name = "InsertRowClause"),
    JsonSubTypes.Type(value = DuplicateKeyClause::class, name = "DuplicateKeyClause"),
    JsonSubTypes.Type(value = LoadDataStatement::class, name = "LoadDataStatement"),
    JsonSubTypes.Type(value = LoadXMLStatement::class, name = "LoadXMLStatement"),
    JsonSubTypes.Type(value = ReplaceStatement::class, name = "ReplaceStatement"),
    JsonSubTypes.Type(value = SetReplaceStatement::class, name = "SetReplaceStatement"),
    JsonSubTypes.Type(value = QueryReplaceStatement::class, name = "QueryReplaceStatement"),
    JsonSubTypes.Type(value = RowReplaceStatement::class, name = "RowReplaceStatement"),
    JsonSubTypes.Type(value = CommonSelectStatement::class, name = "CommonSelectStatement"),
    JsonSubTypes.Type(value = SelectStatement::class, name = "SelectStatement"),
    JsonSubTypes.Type(value = UpdateStatement::class, name = "UpdateStatement"),
    JsonSubTypes.Type(value = SingleUpdateStatement::class, name = "SingleUpdateStatement"),
    JsonSubTypes.Type(value = MultipleUpdateStatement::class, name = "MultipleUpdateStatement"),
    JsonSubTypes.Type(value = SortItem::class, name = "SortItem"),
    JsonSubTypes.Type(value = TableReferenceClause::class, name = "TableReferenceClause"),
    JsonSubTypes.Type(value = NestedTableClause::class, name = "NestedTableClause"),
    JsonSubTypes.Type(value = JoinClause::class, name = "JoinClause"),
    JsonSubTypes.Type(value = SubqueryClause::class, name = "SubqueryClause"),
    JsonSubTypes.Type(value = TableSource::class, name = "TableSource"),
    JsonSubTypes.Type(value = IndexHintList::class, name = "IndexHintList"),
    JsonSubTypes.Type(value = NestedSelectStatement::class, name = "NestedSelectStatement"),
    JsonSubTypes.Type(value = UnionStatement::class, name = "UnionStatement"),
    JsonSubTypes.Type(value = UnionClause::class, name = "UnionClause"),
    JsonSubTypes.Type(value = ColumnClause::class, name = "ColumnClause"),
    JsonSubTypes.Type(value = SelectExportClause::class, name = "SelectExportClause"),
    JsonSubTypes.Type(value = ExportList::class, name = "ExportList"),
    JsonSubTypes.Type(value = ExportDumpFile::class, name = "ExportDumpFile"),
    JsonSubTypes.Type(value = ExportTextFile::class, name = "ExportTextFile"),
    JsonSubTypes.Type(value = FromClause::class, name = "FromClause"),
    JsonSubTypes.Type(value = WhereClause::class, name = "WhereClause"),
    JsonSubTypes.Type(value = GroupByClause::class, name = "GroupByClause"),
    JsonSubTypes.Type(value = GroupByOperator::class, name = "GroupByOperator"),
    JsonSubTypes.Type(value = SimpleGroupByOperator::class, name = "SimpleGroupByOperator"),
    JsonSubTypes.Type(value = SetGroupByOperator::class, name = "SetGroupByOperator"),
    JsonSubTypes.Type(value = StartTransactionStatement::class, name = "StartTransactionStatement"),
    JsonSubTypes.Type(value = BeginWorkStatement::class, name = "BeginWorkStatement"),
    JsonSubTypes.Type(value = CommitWorkStatement::class, name = "CommitWorkStatement"),
    JsonSubTypes.Type(value = RollbackWorkStatement::class, name = "RollbackWorkStatement"),
    JsonSubTypes.Type(value = SavepointStatement::class, name = "SavepointStatement"),
    JsonSubTypes.Type(value = RollbackStatement::class, name = "RollbackStatement"),
    JsonSubTypes.Type(value = ReleaseStatement::class, name = "ReleaseStatement"),
    JsonSubTypes.Type(value = LockTablesStatement::class, name = "LockTablesStatement"),
    JsonSubTypes.Type(value = UnlockTablesStatement::class, name = "UnlockTablesStatement"),
    JsonSubTypes.Type(value = SetAutocommitStatement::class, name = "SetAutocommitStatement"),
    JsonSubTypes.Type(value = SetTransactionStatement::class, name = "SetTransactionStatement"),
    JsonSubTypes.Type(value = LockTableClause::class, name = "LockTableClause"),
    JsonSubTypes.Type(value = TransactionDescriptor::class, name = "TransactionDescriptor"),
    JsonSubTypes.Type(value = ChangeMasterStatement::class, name = "ChangeMasterStatement"),
    JsonSubTypes.Type(value = ChangeFilterStatement::class, name = "ChangeFilterStatement"),
    JsonSubTypes.Type(value = PurgeLogsStatement::class, name = "PurgeLogsStatement"),
    JsonSubTypes.Type(value = ResetMasterStatement::class, name = "ResetMasterStatement"),
    JsonSubTypes.Type(value = ResetSlaveStatement::class, name = "ResetSlaveStatement"),
    JsonSubTypes.Type(value = StartSlaveStatement::class, name = "StartSlaveStatement"),
    JsonSubTypes.Type(value = StopSlaveStatement::class, name = "StopSlaveStatement"),
    JsonSubTypes.Type(value = StartGroupStatement::class, name = "StartGroupStatement"),
    JsonSubTypes.Type(value = StopGroupStatement::class, name = "StopGroupStatement"),
    JsonSubTypes.Type(value = GTID::class, name = "GTID"),
    JsonSubTypes.Type(value = UUID::class, name = "UUID"),
    JsonSubTypes.Type(value = TablePair::class, name = "TablePair"),
    JsonSubTypes.Type(value = XAStartTransactionStatement::class, name = "XAStartTransactionStatement"),
    JsonSubTypes.Type(value = XAEndTransactionStatement::class, name = "XAEndTransactionStatement"),
    JsonSubTypes.Type(value = XAPrepareStatement::class, name = "XAPrepareStatement"),
    JsonSubTypes.Type(value = XACommitStatement::class, name = "XACommitStatement"),
    JsonSubTypes.Type(value = XARollbackStatement::class, name = "XARollbackStatement"),
    JsonSubTypes.Type(value = XARecoverStatement::class, name = "XARecoverStatement"),
    JsonSubTypes.Type(value = PrepareStatement::class, name = "PrepareStatement"),
    JsonSubTypes.Type(value = ExecuteStatement::class, name = "ExecuteStatement"),
    JsonSubTypes.Type(value = DeallocateStatement::class, name = "DeallocateStatement"),
    JsonSubTypes.Type(value = RoutineStatement::class, name = "RoutineStatement"),
    JsonSubTypes.Type(value = BlockQueryStatement::class, name = "BlockQueryStatement"),
    JsonSubTypes.Type(value = CaseStatement::class, name = "CaseStatement"),
    JsonSubTypes.Type(value = IfStatement::class, name = "IfStatement"),
    JsonSubTypes.Type(value = IterateStatement::class, name = "IterateStatement"),
    JsonSubTypes.Type(value = LeaveStatement::class, name = "LeaveStatement"),
    JsonSubTypes.Type(value = LoopStatement::class, name = "LoopStatement"),
    JsonSubTypes.Type(value = RepeatStatement::class, name = "RepeatStatement"),
    JsonSubTypes.Type(value = ReturnStatement::class, name = "ReturnStatement"),
    JsonSubTypes.Type(value = WhileStatement::class, name = "WhileStatement"),
    JsonSubTypes.Type(value = OpenCursorStatement::class, name = "OpenCursorStatement"),
    JsonSubTypes.Type(value = FetchCursorStatement::class, name = "FetchCursorStatement"),
    JsonSubTypes.Type(value = CloseCursorStatement::class, name = "CloseCursorStatement"),
    JsonSubTypes.Type(value = StatementDeclaration::class, name = "StatementDeclaration"),
    JsonSubTypes.Type(value = VariableDeclaration::class, name = "VariableDeclaration"),
    JsonSubTypes.Type(value = ConditionDeclaration::class, name = "ConditionDeclaration"),
    JsonSubTypes.Type(value = CursorDeclaration::class, name = "CursorDeclaration"),
    JsonSubTypes.Type(value = HandlerDeclaration::class, name = "HandlerDeclaration"),
    JsonSubTypes.Type(value = HandlerCondition::class, name = "HandlerCondition"),
    JsonSubTypes.Type(value = HandlerConditionCode::class, name = "HandlerConditionCode"),
    JsonSubTypes.Type(value = HandlerConditionSQLState::class, name = "HandlerConditionSQLState"),
    JsonSubTypes.Type(value = HandlerConditionName::class, name = "HandlerConditionName"),
    JsonSubTypes.Type(value = HandlerConditionWarning::class, name = "HandlerConditionWarning"),
    JsonSubTypes.Type(value = HandlerConditionNotFound::class, name = "HandlerConditionNotFound"),
    JsonSubTypes.Type(value = HandlerConditionException::class, name = "HandlerConditionException"),
    JsonSubTypes.Type(value = ConditionChoiceOption::class, name = "ConditionChoiceOption"),
    JsonSubTypes.Type(value = AlterUserShortStatement::class, name = "AlterUserShortStatement"),
    JsonSubTypes.Type(value = AlterUserFullStatement::class, name = "AlterUserFullStatement"),
    JsonSubTypes.Type(value = CreateUserStatement::class, name = "CreateUserStatement"),
    JsonSubTypes.Type(value = DropUserStatement::class, name = "DropUserStatement"),
    JsonSubTypes.Type(value = GrantStatement::class, name = "GrantStatement"),
    JsonSubTypes.Type(value = GrantProxyStatement::class, name = "GrantProxyStatement"),
    JsonSubTypes.Type(value = RenameUserStatement::class, name = "RenameUserStatement"),
    JsonSubTypes.Type(value = RenameUserClause::class, name = "RenameUserClause"),
    JsonSubTypes.Type(value = RevokeStatement::class, name = "RevokeStatement"),
    JsonSubTypes.Type(value = FullRevokeStatement::class, name = "FullRevokeStatement"),
    JsonSubTypes.Type(value = RevokeProxyStatement::class, name = "RevokeProxyStatement"),
    JsonSubTypes.Type(value = SetPasswordStatement::class, name = "SetPasswordStatement"),
    JsonSubTypes.Type(value = PasswordExpirationClause::class, name = "PasswordExpirationClause"),
    JsonSubTypes.Type(value = UserClause::class, name = "UserClause"),
    JsonSubTypes.Type(value = TLSOptionClause::class, name = "TLSOptionClause"),
    JsonSubTypes.Type(value = PrivilegeClause::class, name = "PrivilegeClause"),
    JsonSubTypes.Type(value = PrivilegeLevelClause::class, name = "PrivilegeLevelClause"),
    JsonSubTypes.Type(value = AnalyzeTableStatement::class, name = "AnalyzeTableStatement"),
    JsonSubTypes.Type(value = CheckTableStatement::class, name = "CheckTableStatement"),
    JsonSubTypes.Type(value = ChecksumTableStatement::class, name = "ChecksumTableStatement"),
    JsonSubTypes.Type(value = OptimizeTableStatement::class, name = "OptimizeTableStatement"),
    JsonSubTypes.Type(value = RepairTableStatement::class, name = "RepairTableStatement"),
    JsonSubTypes.Type(value = CreateUDFunctionStatement::class, name = "CreateUDFunctionStatement"),
    JsonSubTypes.Type(value = InstallPluginStatement::class, name = "InstallPluginStatement"),
    JsonSubTypes.Type(value = UninstallPluginStatement::class, name = "UninstallPluginStatement"),
    JsonSubTypes.Type(value = SetStatement::class, name = "SetStatement"),
    JsonSubTypes.Type(value = SetVariableStatement::class, name = "SetVariableStatement"),
    JsonSubTypes.Type(value = SetCharsetStatement::class, name = "SetCharsetStatement"),
    JsonSubTypes.Type(value = SetNamesStatement::class, name = "SetNamesStatement"),
    JsonSubTypes.Type(value = ShowStatement::class, name = "ShowStatement"),
    JsonSubTypes.Type(value = ShowLogsStatement::class, name = "ShowLogsStatement"),
    JsonSubTypes.Type(value = ShowLogEventsStatement::class, name = "ShowLogEventsStatement"),
    JsonSubTypes.Type(value = ShowEntityStatement::class, name = "ShowEntityStatement"),
    JsonSubTypes.Type(value = ShowColumnsStatement::class, name = "ShowColumnsStatement"),
    JsonSubTypes.Type(value = ShowCreateSchemaStatement::class, name = "ShowCreateSchemaStatement"),
    JsonSubTypes.Type(value = ShowCreateNamedEntityStatement::class, name = "ShowCreateNamedEntityStatement"),
    JsonSubTypes.Type(value = ShowCreateUserStatement::class, name = "ShowCreateUserStatement"),
    JsonSubTypes.Type(value = ShowEngineStatement::class, name = "ShowEngineStatement"),
    JsonSubTypes.Type(value = ShowInfoStatement::class, name = "ShowInfoStatement"),
    JsonSubTypes.Type(value = ShowErrorsStatement::class, name = "ShowErrorsStatement"),
    JsonSubTypes.Type(value = ShowCountErrorsStatement::class, name = "ShowCountErrorsStatement"),
    JsonSubTypes.Type(value = ShowRoutineCodeStatement::class, name = "ShowRoutineCodeStatement"),
    JsonSubTypes.Type(value = ShowGrantsStatement::class, name = "ShowGrantsStatement"),
    JsonSubTypes.Type(value = ShowIndexesStatement::class, name = "ShowIndexesStatement"),
    JsonSubTypes.Type(value = ShowOpenTablesStatement::class, name = "ShowOpenTablesStatement"),
    JsonSubTypes.Type(value = ShowProfileStatement::class, name = "ShowProfileStatement"),
    JsonSubTypes.Type(value = ShowSlaveStatement::class, name = "ShowSlaveStatement"),
    JsonSubTypes.Type(value = ShowFilterClause::class, name = "ShowFilterClause"),
    JsonSubTypes.Type(value = BinlogStatement::class, name = "BinlogStatement"),
    JsonSubTypes.Type(value = CacheIndexStatement::class, name = "CacheIndexStatement"),
    JsonSubTypes.Type(value = FlushStatement::class, name = "FlushStatement"),
    JsonSubTypes.Type(value = KillStatement::class, name = "KillStatement"),
    JsonSubTypes.Type(value = LoadIndexStatement::class, name = "LoadIndexStatement"),
    JsonSubTypes.Type(value = ResetStatement::class, name = "ResetStatement"),
    JsonSubTypes.Type(value = ShutdownStatement::class, name = "ShutdownStatement"),
    JsonSubTypes.Type(value = TableIndexClause::class, name = "TableIndexClause"),
    JsonSubTypes.Type(value = FlushOptionClause::class, name = "FlushOptionClause"),
    JsonSubTypes.Type(value = SimpleFlushOptionClause::class, name = "SimpleFlushOptionClause"),
    JsonSubTypes.Type(value = ChannelFlushOptionClause::class, name = "ChannelFlushOptionClause"),
    JsonSubTypes.Type(value = TablesFlushOptionClause::class, name = "TablesFlushOptionClause"),
    JsonSubTypes.Type(value = TableDescription::class, name = "TableDescription"),
    JsonSubTypes.Type(value = FullTableDescription::class, name = "FullTableDescription"),
    JsonSubTypes.Type(value = HelpStatement::class, name = "HelpStatement"),
    JsonSubTypes.Type(value = UseStatement::class, name = "UseStatement"),
    JsonSubTypes.Type(value = FormatDescriptionClause::class, name = "FormatDescriptionClause"),
    JsonSubTypes.Type(value = ObjectDescriptionClause::class, name = "ObjectDescriptionClause"),
    JsonSubTypes.Type(value = FullName::class, name = "FullName"),
    JsonSubTypes.Type(value = TableName::class, name = "TableName"),
    JsonSubTypes.Type(value = ColumnName::class, name = "ColumnName"),
    JsonSubTypes.Type(value = IndexColumnNameClause::class, name = "IndexColumnNameClause"),
    JsonSubTypes.Type(value = UserName::class, name = "UserName"),
    JsonSubTypes.Type(value = FixedUserName::class, name = "FixedUserName"),
    JsonSubTypes.Type(value = Variable::class, name = "Variable"),
    JsonSubTypes.Type(value = CharSet::class, name = "CharSet"),
    JsonSubTypes.Type(value = XIDName::class, name = "XIDName"),
    JsonSubTypes.Type(value = AuthPlugin::class, name = "AuthPlugin"),
    JsonSubTypes.Type(value = DbName::class, name = "DbName"),
    JsonSubTypes.Type(value = SchemaName::class, name = "SchemaName"),
    JsonSubTypes.Type(value = IndexName::class, name = "IndexName"),
    JsonSubTypes.Type(value = ViewName::class, name = "ViewName"),
    JsonSubTypes.Type(value = TriggerName::class, name = "TriggerName"),
    JsonSubTypes.Type(value = EventName::class, name = "EventName"),
    JsonSubTypes.Type(value = ProcedureName::class, name = "ProcedureName"),
    JsonSubTypes.Type(value = UDFunctionName::class, name = "UDFunctionName"),
    JsonSubTypes.Type(value = TablespaceName::class, name = "TablespaceName"),
    JsonSubTypes.Type(value = LogFileGroupName::class, name = "LogFileGroupName"),
    JsonSubTypes.Type(value = ServerName::class, name = "ServerName"),
    JsonSubTypes.Type(value = Range::class, name = "Range"),
    JsonSubTypes.Type(value = Star::class, name = "Star"),
    JsonSubTypes.Type(value = Identifier::class, name = "Identifier"),
    JsonSubTypes.Type(value = Literal::class, name = "Literal"),
    JsonSubTypes.Type(value = StringLiteral::class, name = "StringLiteral"),
    JsonSubTypes.Type(value = RealLiteral::class, name = "RealLiteral"),
    JsonSubTypes.Type(value = HexadecimalLiteral::class, name = "HexadecimalLiteral"),
    JsonSubTypes.Type(value = BitStringLiteral::class, name = "BitStringLiteral"),
    JsonSubTypes.Type(value = NullLiteral::class, name = "NullLiteral"),
    JsonSubTypes.Type(value = NotNullLiteral::class, name = "NotNullLiteral"),
    JsonSubTypes.Type(value = BooleanLiteral::class, name = "BooleanLiteral"),
    JsonSubTypes.Type(value = NumberLiteral::class, name = "NumberLiteral"),
    JsonSubTypes.Type(value = DataTypeClause::class, name = "DataTypeClause"),
    JsonSubTypes.Type(value = SimpleDataTypeClause::class, name = "SimpleDataTypeClause"),
    JsonSubTypes.Type(value = SpatialDataTypeClause::class, name = "SpatialDataTypeClause"),
    JsonSubTypes.Type(value = DimensionDataTypeClause::class, name = "DimensionDataTypeClause"),
    JsonSubTypes.Type(value = CharDataTypeClause::class, name = "CharDataTypeClause"),
    JsonSubTypes.Type(value = CollectionCharDataTypeClause::class, name = "CollectionCharDataTypeClause"),
    JsonSubTypes.Type(value = ConvertedDataType::class, name = "ConvertedDataType"),
    JsonSubTypes.Type(value = FunctionCall::class, name = "FunctionCall"),
    JsonSubTypes.Type(value = UDFunctionCall::class, name = "UDFunctionCall"),
    JsonSubTypes.Type(value = SimpleFunctionCall::class, name = "SimpleFunctionCall"),
    JsonSubTypes.Type(value = AggregateFunctionCall::class, name = "AggregateFunctionCall"),
    JsonSubTypes.Type(value = CaseFunctionCall::class, name = "CaseFunctionCall"),
    JsonSubTypes.Type(value = CaseClause::class, name = "CaseClause"),
    JsonSubTypes.Type(value = ShortFormFunctionCall::class, name = "ShortFormFunctionCall"),
    JsonSubTypes.Type(value = ComplexFunctionCall::class, name = "ComplexFunctionCall"),
    JsonSubTypes.Type(value = PasswordFunctionCall::class, name = "PasswordFunctionCall"),
    JsonSubTypes.Type(value = OverClause::class, name = "OverClause"),
    JsonSubTypes.Type(value = ComplexArgument::class, name = "ComplexArgument"),
    JsonSubTypes.Type(value = ExpressionArgument::class, name = "ExpressionArgument"),
    JsonSubTypes.Type(value = KeywordArgument::class, name = "KeywordArgument"),
    JsonSubTypes.Type(value = TypedArgument::class, name = "TypedArgument"),
    JsonSubTypes.Type(value = CharsetArgument::class, name = "CharsetArgument"),
    JsonSubTypes.Type(value = NestedArgument::class, name = "NestedArgument"),
    JsonSubTypes.Type(value = Expression::class, name = "Expression"),
    JsonSubTypes.Type(value = Predicate::class, name = "Predicate"),
    JsonSubTypes.Type(value = Primitive::class, name = "Primitive"),
    JsonSubTypes.Type(value = LogicalExpression::class, name = "LogicalExpression"),
    JsonSubTypes.Type(value = IsExpression::class, name = "IsExpression"),
    JsonSubTypes.Type(value = IsNullPredicate::class, name = "IsNullPredicate"),
    JsonSubTypes.Type(value = ComparisonPredicate::class, name = "ComparisonPredicate"),
    JsonSubTypes.Type(value = ComparisonSetPredicate::class, name = "ComparisonSetPredicate"),
    JsonSubTypes.Type(value = InPredicate::class, name = "InPredicate"),
    JsonSubTypes.Type(value = BetweenPredicate::class, name = "BetweenPredicate"),
    JsonSubTypes.Type(value = LikePredicate::class, name = "LikePredicate"),
    JsonSubTypes.Type(value = UnaryExpression::class, name = "UnaryExpression"),
    JsonSubTypes.Type(value = BinaryExpression::class, name = "BinaryExpression"),
    JsonSubTypes.Type(value = ParenthesisExpression::class, name = "ParenthesisExpression"),
    JsonSubTypes.Type(value = ExistsExpression::class, name = "ExistsExpression"),
    JsonSubTypes.Type(value = SubqueryExpression::class, name = "SubqueryExpression"),
    JsonSubTypes.Type(value = IntervalExpression::class, name = "IntervalExpression"),
    JsonSubTypes.Type(value = KeywordPrimitive::class, name = "KeywordPrimitive"),
    JsonSubTypes.Type(value = RowPrimitive::class, name = "RowPrimitive"),
    JsonSubTypes.Type(value = StringPrimitive::class, name = "StringPrimitive"),
    JsonSubTypes.Type(value = CommonSimpleOption::class, name = "CommonSimpleOption"),
    JsonSubTypes.Type(value = StringSimpleOption::class, name = "StringSimpleOption"),
    JsonSubTypes.Type(value = ListStringSimpleOption::class, name = "ListStringSimpleOption"),
    JsonSubTypes.Type(value = NumberSimpleOption::class, name = "NumberSimpleOption"),
    JsonSubTypes.Type(value = BooleanSimpleOption::class, name = "BooleanSimpleOption"),
    JsonSubTypes.Type(value = NodeSimpleOption::class, name = "NodeSimpleOption"),
    JsonSubTypes.Type(value = ListSimpleOption::class, name = "ListSimpleOption"))
open class Serializer


@JsonTypeName("Node")
open class Node: Serializer() {

}

@JsonTypeName("Script")
class Script (
    body: MutableList<Statement>,
    isCommented: Boolean     
): Node() {
    @JsonProperty("body")
    var body: MutableList<Statement> = body
    @JsonProperty("isCommented")
    var isCommented: Boolean = isCommented
}

@JsonTypeName("CommonStatement")
open class CommonStatement: Node() {

}

@JsonTypeName("Statement")
open class Statement: CommonStatement() {

}

@JsonTypeName("SingleQueryStatement")
open class SingleQueryStatement: Statement() {

}

@JsonTypeName("EmptyStatement")
class EmptyStatement: Statement() {

}

@JsonTypeName("WithStatement")
class WithStatement (
    body: Statement     
): Statement() {
    @JsonProperty("body")
    var body: Statement = body
}

@JsonTypeName("CreateDatabaseStatement")
class CreateDatabaseStatement (
    dbFormat: SyntaxFormat,
    ifNotExist: Boolean,
    dbName: SchemaName,
    options: MutableList<CommonSimpleOption>     
): SingleQueryStatement() {
    @JsonProperty("dbFormat")
    var dbFormat: SyntaxFormat = dbFormat
    @JsonProperty("ifNotExist")
    var ifNotExist: Boolean = ifNotExist
    @JsonProperty("dbName")
    var dbName: SchemaName = dbName
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
}

@JsonTypeName("CreateEventStatement")
class CreateEventStatement (
    name: EventName,
    eventSchedule: EventScheduleClause,
    body: Statement,
    definer: Node? = null,
    ifNotExist: Boolean? = null,
    isPreserve: Boolean? = null,
    enableType: EnableEventType? = null,
    comment: String? = null     
): SingleQueryStatement() {
    @JsonProperty("name")
    var name: EventName = name
    @JsonProperty("eventSchedule")
    var eventSchedule: EventScheduleClause = eventSchedule
    @JsonProperty("body")
    var body: Statement = body
    @JsonProperty("definer")
    var definer: Node? = definer
    @JsonProperty("ifNotExist")
    var ifNotExist: Boolean? = ifNotExist
    @JsonProperty("isPreserve")
    var isPreserve: Boolean? = isPreserve
    @JsonProperty("enableType")
    var enableType: EnableEventType? = enableType
    @JsonProperty("comment")
    var comment: String? = comment
}

@JsonTypeName("CreateIndexStatement")
class CreateIndexStatement (
    category: IndexCategory? = null,
    name: IndexName,
    indexType: IndexType? = null,
    table: TableName,
    indexColumns: MutableList<IndexColumnNameClause>,
    options: MutableList<CommonSimpleOption>,
    algorithm: IndexAlgorithmOption? = null,
    lockOption: LockOption? = null,
    creationPlace: IntimeActionType? = null     
): SingleQueryStatement() {
    @JsonProperty("category")
    var category: IndexCategory? = category
    @JsonProperty("name")
    var name: IndexName = name
    @JsonProperty("indexType")
    var indexType: IndexType? = indexType
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("indexColumns")
    var indexColumns: MutableList<IndexColumnNameClause> = indexColumns
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
    @JsonProperty("algorithm")
    var algorithm: IndexAlgorithmOption? = algorithm
    @JsonProperty("lockOption")
    var lockOption: LockOption? = lockOption
    @JsonProperty("creationPlace")
    var creationPlace: IntimeActionType? = creationPlace
}

@JsonTypeName("CreateLogFileGroupStatement")
class CreateLogFileGroupStatement (
    name: LogFileGroupName,
    undoFile: String,
    initialSize: String? = null,
    undoBufferSize: String? = null,
    redoBufferSize: String? = null,
    nodeGroup: Identifier? = null,
    isWait: Boolean? = null,
    comment: String? = null,
    engine: String     
): SingleQueryStatement() {
    @JsonProperty("name")
    var name: LogFileGroupName = name
    @JsonProperty("undoFile")
    var undoFile: String = undoFile
    @JsonProperty("initialSize")
    var initialSize: String? = initialSize
    @JsonProperty("undoBufferSize")
    var undoBufferSize: String? = undoBufferSize
    @JsonProperty("redoBufferSize")
    var redoBufferSize: String? = redoBufferSize
    @JsonProperty("nodeGroup")
    var nodeGroup: Identifier? = nodeGroup
    @JsonProperty("isWait")
    var isWait: Boolean? = isWait
    @JsonProperty("comment")
    var comment: String? = comment
    @JsonProperty("engine")
    var engine: String = engine
}

@JsonTypeName("CreateProcedureStatement")
class CreateProcedureStatement (
    definer: Node? = null,
    procedure: ProcedureName,
    params: MutableList<RoutineParameter>,
    body: Statement,
    options: MutableList<CommonSimpleOption>     
): SingleQueryStatement() {
    @JsonProperty("definer")
    var definer: Node? = definer
    @JsonProperty("procedure")
    var procedure: ProcedureName = procedure
    @JsonProperty("params")
    var params: MutableList<RoutineParameter> = params
    @JsonProperty("body")
    var body: Statement = body
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
}

@JsonTypeName("CreateFunctionStatement")
class CreateFunctionStatement (
    definer: Node? = null,
    function: UDFunctionName,
    params: MutableList<RoutineParameter>,
    body: Statement,
    returnType: DataTypeClause,
    options: MutableList<CommonSimpleOption>     
): SingleQueryStatement() {
    @JsonProperty("definer")
    var definer: Node? = definer
    @JsonProperty("function")
    var function: UDFunctionName = function
    @JsonProperty("params")
    var params: MutableList<RoutineParameter> = params
    @JsonProperty("body")
    var body: Statement = body
    @JsonProperty("returnType")
    var returnType: DataTypeClause = returnType
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
}

@JsonTypeName("CreateServerStatement")
class CreateServerStatement (
    name: ServerName,
    ifExists: Boolean? = null,
    wrapper: Identifier? = null,
    options: MutableList<CommonSimpleOption>     
): SingleQueryStatement() {
    @JsonProperty("name")
    var name: ServerName = name
    @JsonProperty("ifExists")
    var ifExists: Boolean? = ifExists
    @JsonProperty("wrapper")
    var wrapper: Identifier? = wrapper
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
}

@JsonTypeName("CreateTableStatement")
open class CreateTableStatement: SingleQueryStatement() {

}

@JsonTypeName("CopyCreateTableStatement")
class CopyCreateTableStatement (
    isTemporary: Boolean,
    ifNotExist: Boolean,
    table: TableName,
    tableCopy: TableName,
    isParenthesisCopyTable: Boolean     
): CreateTableStatement() {
    @JsonProperty("isTemporary")
    var isTemporary: Boolean = isTemporary
    @JsonProperty("ifNotExist")
    var ifNotExist: Boolean = ifNotExist
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("tableCopy")
    var tableCopy: TableName = tableCopy
    @JsonProperty("isParenthesisCopyTable")
    var isParenthesisCopyTable: Boolean = isParenthesisCopyTable
}

@JsonTypeName("QueryCreateTableStatement")
class QueryCreateTableStatement (
    isTemporary: Boolean,
    ifNotExist: Boolean,
    keyViolation: InsertViolateBehaviour? = null,
    table: TableName,
    queryAs: Boolean,
    query: CommonSelectStatement,
    columns: MutableList<ColumnDeclaration>,
    constraints: MutableList<ConstraintDeclaration>,
    options: MutableList<CommonSimpleOption>,
    partitions: PartitionClause? = null     
): CreateTableStatement() {
    @JsonProperty("isTemporary")
    var isTemporary: Boolean = isTemporary
    @JsonProperty("ifNotExist")
    var ifNotExist: Boolean = ifNotExist
    @JsonProperty("keyViolation")
    var keyViolation: InsertViolateBehaviour? = keyViolation
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("queryAs")
    var queryAs: Boolean = queryAs
    @JsonProperty("query")
    var query: CommonSelectStatement = query
    @JsonProperty("columns")
    var columns: MutableList<ColumnDeclaration> = columns
    @JsonProperty("constraints")
    var constraints: MutableList<ConstraintDeclaration> = constraints
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
    @JsonProperty("partitions")
    var partitions: PartitionClause? = partitions
}

@JsonTypeName("ColumnCreateTableStatement")
class ColumnCreateTableStatement (
    isTemporary: Boolean,
    ifNotExist: Boolean,
    table: TableName,
    columns: MutableList<ColumnDeclaration>,
    constraints: MutableList<ConstraintDeclaration>,
    options: MutableList<CommonSimpleOption>,
    partitions: PartitionClause? = null     
): CreateTableStatement() {
    @JsonProperty("isTemporary")
    var isTemporary: Boolean = isTemporary
    @JsonProperty("ifNotExist")
    var ifNotExist: Boolean = ifNotExist
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("columns")
    var columns: MutableList<ColumnDeclaration> = columns
    @JsonProperty("constraints")
    var constraints: MutableList<ConstraintDeclaration> = constraints
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
    @JsonProperty("partitions")
    var partitions: PartitionClause? = partitions
}

@JsonTypeName("CreateTableSpaceStatement")
class CreateTableSpaceStatement (
    name: TablespaceName,
    dataFileName: String,
    fileBlockSize: String? = null,
    fileGroup: LogFileGroupName? = null,
    extentSize: String? = null,
    initialSize: String? = null,
    autoExtendSize: String? = null,
    maxSize: String? = null,
    nodeGroup: Identifier? = null,
    isWait: Boolean? = null,
    comment: String? = null,
    engine: String? = null     
): SingleQueryStatement() {
    @JsonProperty("name")
    var name: TablespaceName = name
    @JsonProperty("dataFileName")
    var dataFileName: String = dataFileName
    @JsonProperty("fileBlockSize")
    var fileBlockSize: String? = fileBlockSize
    @JsonProperty("fileGroup")
    var fileGroup: LogFileGroupName? = fileGroup
    @JsonProperty("extentSize")
    var extentSize: String? = extentSize
    @JsonProperty("initialSize")
    var initialSize: String? = initialSize
    @JsonProperty("autoExtendSize")
    var autoExtendSize: String? = autoExtendSize
    @JsonProperty("maxSize")
    var maxSize: String? = maxSize
    @JsonProperty("nodeGroup")
    var nodeGroup: Identifier? = nodeGroup
    @JsonProperty("isWait")
    var isWait: Boolean? = isWait
    @JsonProperty("comment")
    var comment: String? = comment
    @JsonProperty("engine")
    var engine: String? = engine
}

@JsonTypeName("CreateTriggerStatement")
class CreateTriggerStatement (
    name: TriggerName,
    table: TableName,
    time: TimeTrigger,
    event: EventTrigger,
    body: Statement,
    definer: Node? = null,
    triggerOrder: TriggerOrderClause? = null     
): SingleQueryStatement() {
    @JsonProperty("name")
    var name: TriggerName = name
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("time")
    var time: TimeTrigger = time
    @JsonProperty("event")
    var event: EventTrigger = event
    @JsonProperty("body")
    var body: Statement = body
    @JsonProperty("definer")
    var definer: Node? = definer
    @JsonProperty("triggerOrder")
    var triggerOrder: TriggerOrderClause? = triggerOrder
}

@JsonTypeName("TriggerOrderClause")
class TriggerOrderClause (
    orderType: OrderTriggerType,
    trigger: TriggerName     
): Node() {
    @JsonProperty("orderType")
    var orderType: OrderTriggerType = orderType
    @JsonProperty("trigger")
    var trigger: TriggerName = trigger
}

@JsonTypeName("CreateViewStatement")
class CreateViewStatement (
    isReplace: Boolean? = null,
    algorithm: AlgorithmView? = null,
    definer: Node? = null,
    sqlSecurity: SecurityOwnerContext? = null,
    name: ViewName,
    columns: MutableList<Identifier>,
    select: CommonSelectStatement? = null,
    checkOption: CheckOptionView? = null     
): SingleQueryStatement() {
    @JsonProperty("isReplace")
    var isReplace: Boolean? = isReplace
    @JsonProperty("algorithm")
    var algorithm: AlgorithmView? = algorithm
    @JsonProperty("definer")
    var definer: Node? = definer
    @JsonProperty("sqlSecurity")
    var sqlSecurity: SecurityOwnerContext? = sqlSecurity
    @JsonProperty("name")
    var name: ViewName = name
    @JsonProperty("columns")
    var columns: MutableList<Identifier> = columns
    @JsonProperty("select")
    var select: CommonSelectStatement? = select
    @JsonProperty("checkOption")
    var checkOption: CheckOptionView? = checkOption
}

@JsonTypeName("EventScheduleClause")
open class EventScheduleClause: Node() {

}

@JsonTypeName("EventSchedulePresicion")
class EventSchedulePresicion (
    timestamp: Expression,
    intervals: MutableList<IntervalExpression>     
): EventScheduleClause() {
    @JsonProperty("timestamp")
    var timestamp: Expression = timestamp
    @JsonProperty("intervals")
    var intervals: MutableList<IntervalExpression> = intervals
}

@JsonTypeName("EventScheduleInterval")
class EventScheduleInterval (
    repeatInterval: IntervalExpression,
    start: Expression? = null,
    startIntervals: MutableList<IntervalExpression>,
    stop: Expression? = null,
    stopIntervals: MutableList<IntervalExpression>     
): EventScheduleClause() {
    @JsonProperty("repeatInterval")
    var repeatInterval: IntervalExpression = repeatInterval
    @JsonProperty("start")
    var start: Expression? = start
    @JsonProperty("startIntervals")
    var startIntervals: MutableList<IntervalExpression> = startIntervals
    @JsonProperty("stop")
    var stop: Expression? = stop
    @JsonProperty("stopIntervals")
    var stopIntervals: MutableList<IntervalExpression> = stopIntervals
}

@JsonTypeName("RoutineParameter")
class RoutineParameter (
    direction: ParameterDirection? = null,
    name: Identifier,
    dataType: DataTypeClause     
): Node() {
    @JsonProperty("direction")
    var direction: ParameterDirection? = direction
    @JsonProperty("name")
    var name: Identifier = name
    @JsonProperty("dataType")
    var dataType: DataTypeClause = dataType
}

@JsonTypeName("ColumnDeclaration")
class ColumnDeclaration (
    name: Identifier,
    dataType: DataTypeClause,
    defaultValue: Literal? = null,
    isNotNull: Boolean,
    isAutoIncrement: Boolean? = null,
    isUnique: Boolean,
    isPrimary: Boolean,
    comment: String? = null,
    columnFormat: ColumnFormat? = null,
    storage: ColumnStorage? = null,
    reference: ReferenceDeclarationClause? = null     
): Node() {
    @JsonProperty("name")
    var name: Identifier = name
    @JsonProperty("dataType")
    var dataType: DataTypeClause = dataType
    @JsonProperty("defaultValue")
    var defaultValue: Literal? = defaultValue
    @JsonProperty("isNotNull")
    var isNotNull: Boolean = isNotNull
    @JsonProperty("isAutoIncrement")
    var isAutoIncrement: Boolean? = isAutoIncrement
    @JsonProperty("isUnique")
    var isUnique: Boolean = isUnique
    @JsonProperty("isPrimary")
    var isPrimary: Boolean = isPrimary
    @JsonProperty("comment")
    var comment: String? = comment
    @JsonProperty("columnFormat")
    var columnFormat: ColumnFormat? = columnFormat
    @JsonProperty("storage")
    var storage: ColumnStorage? = storage
    @JsonProperty("reference")
    var reference: ReferenceDeclarationClause? = reference
}

@JsonTypeName("ConstraintDeclaration")
open class ConstraintDeclaration: Node() {

}

@JsonTypeName("ConstraintKeyClause")
class ConstraintKeyClause (
    name: Identifier? = null,
    keyType: KeyType,
    indexColumns: MutableList<IndexColumnNameClause>,
    indexNameFormat: SyntaxFormat? = null,
    indexName: Identifier? = null,
    indexType: IndexType? = null,
    indexOptionSet: MutableList<CommonSimpleOption>,
    reference: ReferenceDeclarationClause? = null     
): ConstraintDeclaration() {
    @JsonProperty("name")
    var name: Identifier? = name
    @JsonProperty("keyType")
    var keyType: KeyType = keyType
    @JsonProperty("indexColumns")
    var indexColumns: MutableList<IndexColumnNameClause> = indexColumns
    @JsonProperty("indexNameFormat")
    var indexNameFormat: SyntaxFormat? = indexNameFormat
    @JsonProperty("indexName")
    var indexName: Identifier? = indexName
    @JsonProperty("indexType")
    var indexType: IndexType? = indexType
    @JsonProperty("indexOptionSet")
    var indexOptionSet: MutableList<CommonSimpleOption> = indexOptionSet
    @JsonProperty("reference")
    var reference: ReferenceDeclarationClause? = reference
}

@JsonTypeName("ConstraintCheckClause")
class ConstraintCheckClause (
    expression: Expression     
): ConstraintDeclaration() {
    @JsonProperty("expression")
    var expression: Expression = expression
}

@JsonTypeName("ReferenceDeclarationClause")
class ReferenceDeclarationClause (
    table: TableName,
    indexColumns: MutableList<IndexColumnNameClause>,
    matchType: ForeignKeyMatchType? = null,
    onDelete: ReferenceConstraintType? = null,
    onUpdate: ReferenceConstraintType? = null     
): Node() {
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("indexColumns")
    var indexColumns: MutableList<IndexColumnNameClause> = indexColumns
    @JsonProperty("matchType")
    var matchType: ForeignKeyMatchType? = matchType
    @JsonProperty("onDelete")
    var onDelete: ReferenceConstraintType? = onDelete
    @JsonProperty("onUpdate")
    var onUpdate: ReferenceConstraintType? = onUpdate
}

@JsonTypeName("PartitionClause")
class PartitionClause (
    count: Int? = null,
    function: PartitionFunction,
    partitions: MutableList<PartitionDefinition>,
    subFunction: SubPartitionFunction? = null,
    subCount: Int? = null     
): Node() {
    @JsonProperty("count")
    var count: Int? = count
    @JsonProperty("function")
    var function: PartitionFunction = function
    @JsonProperty("partitions")
    var partitions: MutableList<PartitionDefinition> = partitions
    @JsonProperty("subFunction")
    var subFunction: SubPartitionFunction? = subFunction
    @JsonProperty("subCount")
    var subCount: Int? = subCount
}

@JsonTypeName("PartitionFunction")
open class PartitionFunction: Node() {

}

@JsonTypeName("PartitionHash")
class PartitionHash (
    isLinear: Boolean,
    value: Expression     
): PartitionFunction() {
    @JsonProperty("isLinear")
    var isLinear: Boolean = isLinear
    @JsonProperty("value")
    var value: Expression = value
}

@JsonTypeName("PartitionKey")
class PartitionKey (
    isLinear: Boolean,
    columns: MutableList<ColumnName>,
    algorithmType: String? = null     
): PartitionFunction() {
    @JsonProperty("isLinear")
    var isLinear: Boolean = isLinear
    @JsonProperty("columns")
    var columns: MutableList<ColumnName> = columns
    @JsonProperty("algorithmType")
    var algorithmType: String? = algorithmType
}

@JsonTypeName("PartitionRange")
class PartitionRange (
    value: Expression? = null,
    columns: MutableList<ColumnName>     
): PartitionFunction() {
    @JsonProperty("value")
    var value: Expression? = value
    @JsonProperty("columns")
    var columns: MutableList<ColumnName> = columns
}

@JsonTypeName("PartitionList")
class PartitionList (
    value: Expression? = null,
    columns: MutableList<ColumnName>     
): PartitionFunction() {
    @JsonProperty("value")
    var value: Expression? = value
    @JsonProperty("columns")
    var columns: MutableList<ColumnName> = columns
}

@JsonTypeName("SubPartitionFunction")
open class SubPartitionFunction: Node() {

}

@JsonTypeName("SubPartitionHash")
class SubPartitionHash (
    isLinear: Boolean,
    value: Expression     
): SubPartitionFunction() {
    @JsonProperty("isLinear")
    var isLinear: Boolean = isLinear
    @JsonProperty("value")
    var value: Expression = value
}

@JsonTypeName("SubPartitionKey")
class SubPartitionKey (
    isLinear: Boolean,
    columns: MutableList<ColumnName>,
    algorithmType: String? = null     
): SubPartitionFunction() {
    @JsonProperty("isLinear")
    var isLinear: Boolean = isLinear
    @JsonProperty("columns")
    var columns: MutableList<ColumnName> = columns
    @JsonProperty("algorithmType")
    var algorithmType: String? = algorithmType
}

@JsonTypeName("PartitionDefinition")
open class PartitionDefinition: Node() {

}

@JsonTypeName("ComparasionPartitionDefinition")
class ComparasionPartitionDefinition (
    partition: Identifier,
    options: MutableList<CommonSimpleOption>,
    subPartitions: MutableList<SubPartitionDefinition>,
    value: Expression? = null,
    values: MutableList<Literal>     
): PartitionDefinition() {
    @JsonProperty("partition")
    var partition: Identifier = partition
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
    @JsonProperty("subPartitions")
    var subPartitions: MutableList<SubPartitionDefinition> = subPartitions
    @JsonProperty("value")
    var value: Expression? = value
    @JsonProperty("values")
    var values: MutableList<Literal> = values
}

@JsonTypeName("ListPartitionDefinition")
class ListPartitionDefinition (
    partition: Identifier,
    options: MutableList<CommonSimpleOption>,
    subPartitions: MutableList<SubPartitionDefinition>,
    values: MutableList<Literal>     
): PartitionDefinition() {
    @JsonProperty("partition")
    var partition: Identifier = partition
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
    @JsonProperty("subPartitions")
    var subPartitions: MutableList<SubPartitionDefinition> = subPartitions
    @JsonProperty("values")
    var values: MutableList<Literal> = values
}

@JsonTypeName("SimplePartitionDefinition")
class SimplePartitionDefinition (
    partition: Identifier,
    options: MutableList<CommonSimpleOption>,
    subPartitions: MutableList<SubPartitionDefinition>     
): PartitionDefinition() {
    @JsonProperty("partition")
    var partition: Identifier = partition
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
    @JsonProperty("subPartitions")
    var subPartitions: MutableList<SubPartitionDefinition> = subPartitions
}

@JsonTypeName("SubPartitionDefinition")
class SubPartitionDefinition (
    subPartition: Identifier,
    options: MutableList<CommonSimpleOption>     
): Node() {
    @JsonProperty("subPartition")
    var subPartition: Identifier = subPartition
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
}

@JsonTypeName("AlterDatabaseStatement")
class AlterDatabaseStatement (
    dbFormat: SyntaxFormat,
    dbName: SchemaName? = null,
    options: MutableList<CommonSimpleOption>,
    isUpgradeDataDirectory: Boolean     
): SingleQueryStatement() {
    @JsonProperty("dbFormat")
    var dbFormat: SyntaxFormat = dbFormat
    @JsonProperty("dbName")
    var dbName: SchemaName? = dbName
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
    @JsonProperty("isUpgradeDataDirectory")
    var isUpgradeDataDirectory: Boolean = isUpgradeDataDirectory
}

@JsonTypeName("AlterEventStatement")
class AlterEventStatement (
    name: EventName,
    newName: EventName? = null,
    eventSchedule: EventScheduleClause? = null,
    body: Statement? = null,
    definer: Node? = null,
    ifNotExist: Boolean? = null,
    isPreserve: Boolean? = null,
    enableType: EnableEventType? = null,
    comment: String? = null     
): SingleQueryStatement() {
    @JsonProperty("name")
    var name: EventName = name
    @JsonProperty("newName")
    var newName: EventName? = newName
    @JsonProperty("eventSchedule")
    var eventSchedule: EventScheduleClause? = eventSchedule
    @JsonProperty("body")
    var body: Statement? = body
    @JsonProperty("definer")
    var definer: Node? = definer
    @JsonProperty("ifNotExist")
    var ifNotExist: Boolean? = ifNotExist
    @JsonProperty("isPreserve")
    var isPreserve: Boolean? = isPreserve
    @JsonProperty("enableType")
    var enableType: EnableEventType? = enableType
    @JsonProperty("comment")
    var comment: String? = comment
}

@JsonTypeName("AlterFunctionStatement")
class AlterFunctionStatement (
    function: UDFunctionName,
    options: MutableList<CommonSimpleOption>     
): SingleQueryStatement() {
    @JsonProperty("function")
    var function: UDFunctionName = function
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
}

@JsonTypeName("AlterInstanceStatement")
class AlterInstanceStatement: SingleQueryStatement() {

}

@JsonTypeName("AlterLogFileGroupStatement")
class AlterLogFileGroupStatement (
    name: LogFileGroupName,
    undoFile: String,
    initialSize: String? = null,
    isWait: Boolean? = null,
    engine: String     
): SingleQueryStatement() {
    @JsonProperty("name")
    var name: LogFileGroupName = name
    @JsonProperty("undoFile")
    var undoFile: String = undoFile
    @JsonProperty("initialSize")
    var initialSize: String? = initialSize
    @JsonProperty("isWait")
    var isWait: Boolean? = isWait
    @JsonProperty("engine")
    var engine: String = engine
}

@JsonTypeName("AlterProcedureStatement")
class AlterProcedureStatement (
    procedure: ProcedureName,
    options: MutableList<CommonSimpleOption>     
): SingleQueryStatement() {
    @JsonProperty("procedure")
    var procedure: ProcedureName = procedure
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
}

@JsonTypeName("AlterServerStatement")
class AlterServerStatement (
    name: Identifier,
    options: MutableList<CommonSimpleOption>     
): SingleQueryStatement() {
    @JsonProperty("name")
    var name: Identifier = name
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
}

@JsonTypeName("AlterTableStatement")
class AlterTableStatement (
    table: TableName,
    isIgnore: Boolean,
    creationPlace: IntimeActionType? = null,
    alterSpecificationClauses: MutableList<AlterSpecification>,
    partitions: PartitionClause? = null     
): SingleQueryStatement() {
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("isIgnore")
    var isIgnore: Boolean = isIgnore
    @JsonProperty("creationPlace")
    var creationPlace: IntimeActionType? = creationPlace
    @JsonProperty("alterSpecificationClauses")
    var alterSpecificationClauses: MutableList<AlterSpecification> = alterSpecificationClauses
    @JsonProperty("partitions")
    var partitions: PartitionClause? = partitions
}

@JsonTypeName("AlterTableSpaceStatement")
class AlterTableSpaceStatement (
    name: TablespaceName,
    dataFileName: String,
    dataFileAction: ActionOnObject,
    initialSize: String? = null,
    isWait: Boolean,
    engine: String     
): SingleQueryStatement() {
    @JsonProperty("name")
    var name: TablespaceName = name
    @JsonProperty("dataFileName")
    var dataFileName: String = dataFileName
    @JsonProperty("dataFileAction")
    var dataFileAction: ActionOnObject = dataFileAction
    @JsonProperty("initialSize")
    var initialSize: String? = initialSize
    @JsonProperty("isWait")
    var isWait: Boolean = isWait
    @JsonProperty("engine")
    var engine: String = engine
}

@JsonTypeName("AlterViewStatement")
class AlterViewStatement (
    algorithm: AlgorithmView? = null,
    name: ViewName,
    columns: MutableList<Identifier>,
    select: CommonSelectStatement? = null,
    options: MutableList<CommonSimpleOption>,
    checkOption: CheckOptionView? = null     
): SingleQueryStatement() {
    @JsonProperty("algorithm")
    var algorithm: AlgorithmView? = algorithm
    @JsonProperty("name")
    var name: ViewName = name
    @JsonProperty("columns")
    var columns: MutableList<Identifier> = columns
    @JsonProperty("select")
    var select: CommonSelectStatement? = select
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
    @JsonProperty("checkOption")
    var checkOption: CheckOptionView? = checkOption
}

@JsonTypeName("AlterSpecification")
open class AlterSpecification: Node() {

}

@JsonTypeName("AlterTableOption")
class AlterTableOption (
    option: CommonSimpleOption     
): AlterSpecification() {
    @JsonProperty("option")
    var option: CommonSimpleOption = option
}

@JsonTypeName("AlterAddColumn")
class AlterAddColumn (
    column: ColumnDeclaration,
    isFirst: Boolean? = null,
    afterColumn: ColumnName? = null,
    isColumn: Boolean     
): AlterSpecification() {
    @JsonProperty("column")
    var column: ColumnDeclaration = column
    @JsonProperty("isFirst")
    var isFirst: Boolean? = isFirst
    @JsonProperty("afterColumn")
    var afterColumn: ColumnName? = afterColumn
    @JsonProperty("isColumn")
    var isColumn: Boolean = isColumn
}

@JsonTypeName("AlterAddColumns")
class AlterAddColumns (
    columns: MutableList<ColumnDeclaration>,
    isColumn: Boolean     
): AlterSpecification() {
    @JsonProperty("columns")
    var columns: MutableList<ColumnDeclaration> = columns
    @JsonProperty("isColumn")
    var isColumn: Boolean = isColumn
}

@JsonTypeName("AlterSetDefaultColumn")
class AlterSetDefaultColumn (
    defaultValue: Literal,
    column: ColumnName,
    isColumn: Boolean     
): AlterSpecification() {
    @JsonProperty("defaultValue")
    var defaultValue: Literal = defaultValue
    @JsonProperty("column")
    var column: ColumnName = column
    @JsonProperty("isColumn")
    var isColumn: Boolean = isColumn
}

@JsonTypeName("AlterDropDefaultColumn")
class AlterDropDefaultColumn (
    column: ColumnName,
    isColumn: Boolean     
): AlterSpecification() {
    @JsonProperty("column")
    var column: ColumnName = column
    @JsonProperty("isColumn")
    var isColumn: Boolean = isColumn
}

@JsonTypeName("AlterChangeColumn")
class AlterChangeColumn (
    isColumn: Boolean,
    previousColumn: ColumnName,
    newColumn: ColumnDeclaration,
    isFirst: Boolean? = null,
    afterColumn: ColumnName? = null     
): AlterSpecification() {
    @JsonProperty("isColumn")
    var isColumn: Boolean = isColumn
    @JsonProperty("previousColumn")
    var previousColumn: ColumnName = previousColumn
    @JsonProperty("newColumn")
    var newColumn: ColumnDeclaration = newColumn
    @JsonProperty("isFirst")
    var isFirst: Boolean? = isFirst
    @JsonProperty("afterColumn")
    var afterColumn: ColumnName? = afterColumn
}

@JsonTypeName("AlterModifyColumn")
class AlterModifyColumn (
    isColumn: Boolean,
    column: ColumnDeclaration,
    isFirst: Boolean? = null,
    afterColumn: ColumnName     
): AlterSpecification() {
    @JsonProperty("isColumn")
    var isColumn: Boolean = isColumn
    @JsonProperty("column")
    var column: ColumnDeclaration = column
    @JsonProperty("isFirst")
    var isFirst: Boolean? = isFirst
    @JsonProperty("afterColumn")
    var afterColumn: ColumnName = afterColumn
}

@JsonTypeName("AlterDropColumn")
class AlterDropColumn (
    isColumn: Boolean,
    column: ColumnName     
): AlterSpecification() {
    @JsonProperty("isColumn")
    var isColumn: Boolean = isColumn
    @JsonProperty("column")
    var column: ColumnName = column
}

@JsonTypeName("AlterAddKey")
class AlterAddKey (
    keyType: KeyType,
    constraintName: Identifier? = null,
    indexName: IndexName? = null,
    indexType: IndexType? = null,
    indexColumns: MutableList<IndexColumnNameClause>,
    options: MutableList<CommonSimpleOption>,
    reference: ReferenceDeclarationClause? = null     
): AlterSpecification() {
    @JsonProperty("keyType")
    var keyType: KeyType = keyType
    @JsonProperty("constraintName")
    var constraintName: Identifier? = constraintName
    @JsonProperty("indexName")
    var indexName: IndexName? = indexName
    @JsonProperty("indexType")
    var indexType: IndexType? = indexType
    @JsonProperty("indexColumns")
    var indexColumns: MutableList<IndexColumnNameClause> = indexColumns
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
    @JsonProperty("reference")
    var reference: ReferenceDeclarationClause? = reference
}

@JsonTypeName("AlterDropKey")
class AlterDropKey (
    keyType: KeyType,
    indexName: IndexName? = null     
): AlterSpecification() {
    @JsonProperty("keyType")
    var keyType: KeyType = keyType
    @JsonProperty("indexName")
    var indexName: IndexName? = indexName
}

@JsonTypeName("AlterSpecPartition")
class AlterSpecPartition (
    action: PartitionAction,
    isAll: Boolean? = null,
    partitions: MutableList<Identifier>,
    newPartition: PartitionDefinition,
    coalesceValue: Int? = null,
    reorgPartitions: MutableList<PartitionDefinition>,
    exchgPartition: Identifier? = null,
    exchgTable: TableName? = null,
    exchgValidationFormat: SyntaxFormat? = null     
): AlterSpecification() {
    @JsonProperty("action")
    var action: PartitionAction = action
    @JsonProperty("isAll")
    var isAll: Boolean? = isAll
    @JsonProperty("partitions")
    var partitions: MutableList<Identifier> = partitions
    @JsonProperty("newPartition")
    var newPartition: PartitionDefinition = newPartition
    @JsonProperty("coalesceValue")
    var coalesceValue: Int? = coalesceValue
    @JsonProperty("reorgPartitions")
    var reorgPartitions: MutableList<PartitionDefinition> = reorgPartitions
    @JsonProperty("exchgPartition")
    var exchgPartition: Identifier? = exchgPartition
    @JsonProperty("exchgTable")
    var exchgTable: TableName? = exchgTable
    @JsonProperty("exchgValidationFormat")
    var exchgValidationFormat: SyntaxFormat? = exchgValidationFormat
}

@JsonTypeName("AlterSpecCommon")
class AlterSpecCommon (
    action: AlterAction,
    algorithm: IndexAlgorithmOption? = null,
    lock: LockOption? = null,
    newName: Identifier? = null,
    orders: MutableList<Identifier>,
    charSetName: String? = null,
    collationName: String? = null,
    validationFormat: SyntaxFormat? = null,
    renameFormat: SyntaxFormat? = null     
): AlterSpecification() {
    @JsonProperty("action")
    var action: AlterAction = action
    @JsonProperty("algorithm")
    var algorithm: IndexAlgorithmOption? = algorithm
    @JsonProperty("lock")
    var lock: LockOption? = lock
    @JsonProperty("newName")
    var newName: Identifier? = newName
    @JsonProperty("orders")
    var orders: MutableList<Identifier> = orders
    @JsonProperty("charSetName")
    var charSetName: String? = charSetName
    @JsonProperty("collationName")
    var collationName: String? = collationName
    @JsonProperty("validationFormat")
    var validationFormat: SyntaxFormat? = validationFormat
    @JsonProperty("renameFormat")
    var renameFormat: SyntaxFormat? = renameFormat
}

@JsonTypeName("DropDatabaseStatement")
class DropDatabaseStatement (
    ifExist: Boolean,
    name: SchemaName     
): SingleQueryStatement() {
    @JsonProperty("ifExist")
    var ifExist: Boolean = ifExist
    @JsonProperty("name")
    var name: SchemaName = name
}

@JsonTypeName("DropEventStatement")
class DropEventStatement (
    event: EventName,
    ifExist: Boolean     
): SingleQueryStatement() {
    @JsonProperty("event")
    var event: EventName = event
    @JsonProperty("ifExist")
    var ifExist: Boolean = ifExist
}

@JsonTypeName("DropIndexStatement")
class DropIndexStatement (
    creationPlace: IntimeActionType? = null,
    index: IndexName,
    table: TableName,
    algorithm: IndexAlgorithmOption? = null,
    lock: LockOption? = null     
): SingleQueryStatement() {
    @JsonProperty("creationPlace")
    var creationPlace: IntimeActionType? = creationPlace
    @JsonProperty("index")
    var index: IndexName = index
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("algorithm")
    var algorithm: IndexAlgorithmOption? = algorithm
    @JsonProperty("lock")
    var lock: LockOption? = lock
}

@JsonTypeName("DropLogfileGroupStatement")
class DropLogfileGroupStatement (
    name: LogFileGroupName,
    engine: String     
): SingleQueryStatement() {
    @JsonProperty("name")
    var name: LogFileGroupName = name
    @JsonProperty("engine")
    var engine: String = engine
}

@JsonTypeName("DropProcedureStatement")
class DropProcedureStatement (
    procedure: ProcedureName,
    ifExist: Boolean     
): SingleQueryStatement() {
    @JsonProperty("procedure")
    var procedure: ProcedureName = procedure
    @JsonProperty("ifExist")
    var ifExist: Boolean = ifExist
}

@JsonTypeName("DropFunctionStatement")
class DropFunctionStatement (
    function: UDFunctionName,
    ifExist: Boolean     
): SingleQueryStatement() {
    @JsonProperty("function")
    var function: UDFunctionName = function
    @JsonProperty("ifExist")
    var ifExist: Boolean = ifExist
}

@JsonTypeName("DropServerStatement")
class DropServerStatement (
    server: ServerName,
    ifExist: Boolean     
): SingleQueryStatement() {
    @JsonProperty("server")
    var server: ServerName = server
    @JsonProperty("ifExist")
    var ifExist: Boolean = ifExist
}

@JsonTypeName("DropTableStatement")
class DropTableStatement (
    tables: MutableList<TableName>,
    isTemporary: Boolean,
    ifExist: Boolean,
    dropType: ConstraintDropType? = null     
): SingleQueryStatement() {
    @JsonProperty("tables")
    var tables: MutableList<TableName> = tables
    @JsonProperty("isTemporary")
    var isTemporary: Boolean = isTemporary
    @JsonProperty("ifExist")
    var ifExist: Boolean = ifExist
    @JsonProperty("dropType")
    var dropType: ConstraintDropType? = dropType
}

@JsonTypeName("DropTablespaceStatement")
class DropTablespaceStatement (
    tablespace: TablespaceName,
    engine: String? = null     
): SingleQueryStatement() {
    @JsonProperty("tablespace")
    var tablespace: TablespaceName = tablespace
    @JsonProperty("engine")
    var engine: String? = engine
}

@JsonTypeName("DropTriggerStatement")
class DropTriggerStatement (
    trigger: TriggerName,
    ifExist: Boolean     
): SingleQueryStatement() {
    @JsonProperty("trigger")
    var trigger: TriggerName = trigger
    @JsonProperty("ifExist")
    var ifExist: Boolean = ifExist
}

@JsonTypeName("DropViewStatement")
class DropViewStatement (
    views: MutableList<ViewName>,
    ifExist: Boolean,
    dropType: ConstraintDropType? = null     
): SingleQueryStatement() {
    @JsonProperty("views")
    var views: MutableList<ViewName> = views
    @JsonProperty("ifExist")
    var ifExist: Boolean = ifExist
    @JsonProperty("dropType")
    var dropType: ConstraintDropType? = dropType
}

@JsonTypeName("RenameStatement")
class RenameStatement (
    clauses: MutableList<RenameTableClause>     
): SingleQueryStatement() {
    @JsonProperty("clauses")
    var clauses: MutableList<RenameTableClause> = clauses
}

@JsonTypeName("RenameTableClause")
class RenameTableClause (
    from: TableName,
    to: TableName     
): SingleQueryStatement() {
    @JsonProperty("from")
    var from: TableName = from
    @JsonProperty("to")
    var to: TableName = to
}

@JsonTypeName("TruncateStatement")
class TruncateStatement (
    table: TableName,
    presentTable: Boolean     
): SingleQueryStatement() {
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("presentTable")
    var presentTable: Boolean = presentTable
}

@JsonTypeName("CallStatement")
class CallStatement (
    name: ProcedureName,
    parameters: MutableList<Expression>     
): SingleQueryStatement() {
    @JsonProperty("name")
    var name: ProcedureName = name
    @JsonProperty("parameters")
    var parameters: MutableList<Expression> = parameters
}

@JsonTypeName("DeleteStatement")
open class DeleteStatement: SingleQueryStatement() {

}

@JsonTypeName("SingleDeleteStatement")
class SingleDeleteStatement (
    priority: Priority? = null,
    isIgnore: Boolean,
    isQuick: Boolean,
    table: TableName,
    partitions: MutableList<Identifier>,
    whereClause: WhereClause? = null,
    orders: MutableList<SortItem>,
    limit: Int? = null     
): DeleteStatement() {
    @JsonProperty("priority")
    var priority: Priority? = priority
    @JsonProperty("isIgnore")
    var isIgnore: Boolean = isIgnore
    @JsonProperty("isQuick")
    var isQuick: Boolean = isQuick
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("partitions")
    var partitions: MutableList<Identifier> = partitions
    @JsonProperty("whereClause")
    var whereClause: WhereClause? = whereClause
    @JsonProperty("orders")
    var orders: MutableList<SortItem> = orders
    @JsonProperty("limit")
    var limit: Int? = limit
}

@JsonTypeName("MultipleDeleteStatement")
class MultipleDeleteStatement (
    priority: Priority? = null,
    format: DeletionFormat,
    isIgnore: Boolean,
    isQuick: Boolean,
    tables: MutableList<TableName>,
    references: MutableList<TableReferenceClause>,
    whereClause: WhereClause? = null     
): DeleteStatement() {
    @JsonProperty("priority")
    var priority: Priority? = priority
    @JsonProperty("format")
    var format: DeletionFormat = format
    @JsonProperty("isIgnore")
    var isIgnore: Boolean = isIgnore
    @JsonProperty("isQuick")
    var isQuick: Boolean = isQuick
    @JsonProperty("tables")
    var tables: MutableList<TableName> = tables
    @JsonProperty("references")
    var references: MutableList<TableReferenceClause> = references
    @JsonProperty("whereClause")
    var whereClause: WhereClause? = whereClause
}

@JsonTypeName("DoStatement")
class DoStatement (
    expressions: MutableList<Expression>     
): SingleQueryStatement() {
    @JsonProperty("expressions")
    var expressions: MutableList<Expression> = expressions
}

@JsonTypeName("HandlerStatement")
open class HandlerStatement: SingleQueryStatement() {

}

@JsonTypeName("HandlerOpenStatement")
class HandlerOpenStatement (
    table: TableName,
    presentAs: Boolean,
    alias: Identifier? = null     
): HandlerStatement() {
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("presentAs")
    var presentAs: Boolean = presentAs
    @JsonProperty("alias")
    var alias: Identifier? = alias
}

@JsonTypeName("HandlerReadComparasionStatement")
class HandlerReadComparasionStatement (
    table: TableName,
    index: IndexName,
    operator: ComparisonOperator? = null,
    values: MutableList<Literal>,
    whereClause: WhereClause? = null,
    limit: Int? = null     
): HandlerStatement() {
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("index")
    var index: IndexName = index
    @JsonProperty("operator")
    var operator: ComparisonOperator? = operator
    @JsonProperty("values")
    var values: MutableList<Literal> = values
    @JsonProperty("whereClause")
    var whereClause: WhereClause? = whereClause
    @JsonProperty("limit")
    var limit: Int? = limit
}

@JsonTypeName("HandlerReadOrderedStatement")
class HandlerReadOrderedStatement (
    table: TableName,
    index: IndexName,
    indexOrder: IndexOrder,
    whereClause: WhereClause? = null,
    limit: Int? = null     
): HandlerStatement() {
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("index")
    var index: IndexName = index
    @JsonProperty("indexOrder")
    var indexOrder: IndexOrder = indexOrder
    @JsonProperty("whereClause")
    var whereClause: WhereClause? = whereClause
    @JsonProperty("limit")
    var limit: Int? = limit
}

@JsonTypeName("HandlerReadSimpleStatement")
class HandlerReadSimpleStatement (
    table: TableName,
    indexOrder: IndexOrder,
    whereClause: WhereClause? = null,
    limit: Int? = null     
): HandlerStatement() {
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("indexOrder")
    var indexOrder: IndexOrder = indexOrder
    @JsonProperty("whereClause")
    var whereClause: WhereClause? = whereClause
    @JsonProperty("limit")
    var limit: Int? = limit
}

@JsonTypeName("HandlerCloseStatement")
class HandlerCloseStatement (
    table: TableName     
): HandlerStatement() {
    @JsonProperty("table")
    var table: TableName = table
}

@JsonTypeName("InsertStatement")
open class InsertStatement: SingleQueryStatement() {

}

@JsonTypeName("InsertSetStatement")
class InsertSetStatement (
    priority: Priority? = null,
    isIgnore: Boolean,
    isIntoFormat: Boolean,
    table: TableName,
    partitions: MutableList<Identifier>,
    columns: MutableList<ColumnName>,
    expressions: MutableList<Expression>,
    onDuplicateKey: DuplicateKeyClause? = null     
): InsertStatement() {
    @JsonProperty("priority")
    var priority: Priority? = priority
    @JsonProperty("isIgnore")
    var isIgnore: Boolean = isIgnore
    @JsonProperty("isIntoFormat")
    var isIntoFormat: Boolean = isIntoFormat
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("partitions")
    var partitions: MutableList<Identifier> = partitions
    @JsonProperty("columns")
    var columns: MutableList<ColumnName> = columns
    @JsonProperty("expressions")
    var expressions: MutableList<Expression> = expressions
    @JsonProperty("onDuplicateKey")
    var onDuplicateKey: DuplicateKeyClause? = onDuplicateKey
}

@JsonTypeName("InsertQueryStatement")
class InsertQueryStatement (
    priority: Priority? = null,
    isIgnore: Boolean,
    isIntoFormat: Boolean,
    table: TableName,
    partitions: MutableList<Identifier>,
    columns: MutableList<ColumnName>,
    query: CommonSelectStatement,
    onDuplicateKey: DuplicateKeyClause? = null     
): InsertStatement() {
    @JsonProperty("priority")
    var priority: Priority? = priority
    @JsonProperty("isIgnore")
    var isIgnore: Boolean = isIgnore
    @JsonProperty("isIntoFormat")
    var isIntoFormat: Boolean = isIntoFormat
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("partitions")
    var partitions: MutableList<Identifier> = partitions
    @JsonProperty("columns")
    var columns: MutableList<ColumnName> = columns
    @JsonProperty("query")
    var query: CommonSelectStatement = query
    @JsonProperty("onDuplicateKey")
    var onDuplicateKey: DuplicateKeyClause? = onDuplicateKey
}

@JsonTypeName("InsertRowStatement")
class InsertRowStatement (
    priority: Priority? = null,
    isIgnore: Boolean,
    isIntoFormat: Boolean,
    table: TableName,
    partitions: MutableList<Identifier>,
    columns: MutableList<ColumnName>,
    rows: MutableList<InsertRowClause>,
    onDuplicateKey: DuplicateKeyClause? = null     
): InsertStatement() {
    @JsonProperty("priority")
    var priority: Priority? = priority
    @JsonProperty("isIgnore")
    var isIgnore: Boolean = isIgnore
    @JsonProperty("isIntoFormat")
    var isIntoFormat: Boolean = isIntoFormat
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("partitions")
    var partitions: MutableList<Identifier> = partitions
    @JsonProperty("columns")
    var columns: MutableList<ColumnName> = columns
    @JsonProperty("rows")
    var rows: MutableList<InsertRowClause> = rows
    @JsonProperty("onDuplicateKey")
    var onDuplicateKey: DuplicateKeyClause? = onDuplicateKey
}

@JsonTypeName("InsertRowClause")
class InsertRowClause (
    values: MutableList<Expression>     
): Node() {
    @JsonProperty("values")
    var values: MutableList<Expression> = values
}

@JsonTypeName("DuplicateKeyClause")
class DuplicateKeyClause (
    columns: MutableList<ColumnName>,
    values: MutableList<Expression>     
): Node() {
    @JsonProperty("columns")
    var columns: MutableList<ColumnName> = columns
    @JsonProperty("values")
    var values: MutableList<Expression> = values
}

@JsonTypeName("LoadDataStatement")
class LoadDataStatement (
    priority: Priority? = null,
    keyViolation: InsertViolateBehaviour? = null,
    isLocal: Boolean,
    partitions: MutableList<Identifier>,
    table: TableName,
    ignoreLines: Int? = null,
    linesFormat: SyntaxFormat? = null,
    loadedColumns: MutableList<Primitive>,
    setColumns: MutableList<ColumnName>,
    setValues: MutableList<Expression>,
    fieldsFormat: SyntaxFormat? = null,
    fileUnloadOptions: MutableList<CommonSimpleOption>     
): SingleQueryStatement() {
    @JsonProperty("priority")
    var priority: Priority? = priority
    @JsonProperty("keyViolation")
    var keyViolation: InsertViolateBehaviour? = keyViolation
    @JsonProperty("isLocal")
    var isLocal: Boolean = isLocal
    @JsonProperty("partitions")
    var partitions: MutableList<Identifier> = partitions
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("ignoreLines")
    var ignoreLines: Int? = ignoreLines
    @JsonProperty("linesFormat")
    var linesFormat: SyntaxFormat? = linesFormat
    @JsonProperty("loadedColumns")
    var loadedColumns: MutableList<Primitive> = loadedColumns
    @JsonProperty("setColumns")
    var setColumns: MutableList<ColumnName> = setColumns
    @JsonProperty("setValues")
    var setValues: MutableList<Expression> = setValues
    @JsonProperty("fieldsFormat")
    var fieldsFormat: SyntaxFormat? = fieldsFormat
    @JsonProperty("fileUnloadOptions")
    var fileUnloadOptions: MutableList<CommonSimpleOption> = fileUnloadOptions
}

@JsonTypeName("LoadXMLStatement")
class LoadXMLStatement (
    priority: Priority? = null,
    keyViolation: InsertViolateBehaviour? = null,
    isLocal: Boolean,
    fileName: String,
    table: TableName,
    charSet: String? = null,
    tagDefinition: String? = null,
    ignoreLines: Int? = null,
    linesFormat: SyntaxFormat? = null,
    loadedColumns: MutableList<Primitive>,
    setColumns: MutableList<ColumnName>,
    setValues: MutableList<Expression>     
): SingleQueryStatement() {
    @JsonProperty("priority")
    var priority: Priority? = priority
    @JsonProperty("keyViolation")
    var keyViolation: InsertViolateBehaviour? = keyViolation
    @JsonProperty("isLocal")
    var isLocal: Boolean = isLocal
    @JsonProperty("fileName")
    var fileName: String = fileName
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("charSet")
    var charSet: String? = charSet
    @JsonProperty("tagDefinition")
    var tagDefinition: String? = tagDefinition
    @JsonProperty("ignoreLines")
    var ignoreLines: Int? = ignoreLines
    @JsonProperty("linesFormat")
    var linesFormat: SyntaxFormat? = linesFormat
    @JsonProperty("loadedColumns")
    var loadedColumns: MutableList<Primitive> = loadedColumns
    @JsonProperty("setColumns")
    var setColumns: MutableList<ColumnName> = setColumns
    @JsonProperty("setValues")
    var setValues: MutableList<Expression> = setValues
}

@JsonTypeName("ReplaceStatement")
open class ReplaceStatement: SingleQueryStatement() {

}

@JsonTypeName("SetReplaceStatement")
class SetReplaceStatement (
    priority: Priority? = null,
    isIntoFormat: Boolean,
    table: TableName,
    partitions: MutableList<Identifier>,
    columns: MutableList<ColumnName>,
    expressions: MutableList<Expression>     
): ReplaceStatement() {
    @JsonProperty("priority")
    var priority: Priority? = priority
    @JsonProperty("isIntoFormat")
    var isIntoFormat: Boolean = isIntoFormat
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("partitions")
    var partitions: MutableList<Identifier> = partitions
    @JsonProperty("columns")
    var columns: MutableList<ColumnName> = columns
    @JsonProperty("expressions")
    var expressions: MutableList<Expression> = expressions
}

@JsonTypeName("QueryReplaceStatement")
class QueryReplaceStatement (
    priority: Priority? = null,
    isIntoFormat: Boolean,
    table: TableName,
    partitions: MutableList<Identifier>,
    columns: MutableList<ColumnName>,
    query: CommonSelectStatement     
): ReplaceStatement() {
    @JsonProperty("priority")
    var priority: Priority? = priority
    @JsonProperty("isIntoFormat")
    var isIntoFormat: Boolean = isIntoFormat
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("partitions")
    var partitions: MutableList<Identifier> = partitions
    @JsonProperty("columns")
    var columns: MutableList<ColumnName> = columns
    @JsonProperty("query")
    var query: CommonSelectStatement = query
}

@JsonTypeName("RowReplaceStatement")
class RowReplaceStatement (
    priority: Priority? = null,
    isIntoFormat: Boolean,
    table: TableName,
    partitions: MutableList<Identifier>,
    columns: MutableList<ColumnName>,
    rows: MutableList<InsertRowClause>     
): ReplaceStatement() {
    @JsonProperty("priority")
    var priority: Priority? = priority
    @JsonProperty("isIntoFormat")
    var isIntoFormat: Boolean = isIntoFormat
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("partitions")
    var partitions: MutableList<Identifier> = partitions
    @JsonProperty("columns")
    var columns: MutableList<ColumnName> = columns
    @JsonProperty("rows")
    var rows: MutableList<InsertRowClause> = rows
}

@JsonTypeName("CommonSelectStatement")
open class CommonSelectStatement: SingleQueryStatement() {

}

@JsonTypeName("SelectStatement")
class SelectStatement (
    columns: MutableList<ColumnClause>,
    fromClause: FromClause? = null,
    whereClause: WhereClause? = null,
    groupBy: GroupByClause? = null,
    orders: MutableList<SortItem>,
    having: Expression? = null,
    limitLines: Int? = null,
    limitOffset: Int? = null,
    export: SelectExportClause? = null,
    lockFormat: SyntaxFormat? = null,
    specificators: MutableList<SelectSpecificators>     
): CommonSelectStatement() {
    @JsonProperty("columns")
    var columns: MutableList<ColumnClause> = columns
    @JsonProperty("fromClause")
    var fromClause: FromClause? = fromClause
    @JsonProperty("whereClause")
    var whereClause: WhereClause? = whereClause
    @JsonProperty("groupBy")
    var groupBy: GroupByClause? = groupBy
    @JsonProperty("orders")
    var orders: MutableList<SortItem> = orders
    @JsonProperty("having")
    var having: Expression? = having
    @JsonProperty("limitLines")
    var limitLines: Int? = limitLines
    @JsonProperty("limitOffset")
    var limitOffset: Int? = limitOffset
    @JsonProperty("export")
    var export: SelectExportClause? = export
    @JsonProperty("lockFormat")
    var lockFormat: SyntaxFormat? = lockFormat
    @JsonProperty("specificators")
    var specificators: MutableList<SelectSpecificators> = specificators
}

@JsonTypeName("UpdateStatement")
open class UpdateStatement: SingleQueryStatement() {

}

@JsonTypeName("SingleUpdateStatement")
class SingleUpdateStatement (
    priority: Priority? = null,
    isIgnore: Boolean,
    table: TableName,
    presentAs: Boolean,
    alias: Identifier? = null,
    columns: MutableList<ColumnName>,
    values: MutableList<Expression>,
    whereClause: WhereClause? = null,
    orders: MutableList<SortItem>,
    limitLines: Int? = null,
    limitOffset: Int? = null     
): UpdateStatement() {
    @JsonProperty("priority")
    var priority: Priority? = priority
    @JsonProperty("isIgnore")
    var isIgnore: Boolean = isIgnore
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("presentAs")
    var presentAs: Boolean = presentAs
    @JsonProperty("alias")
    var alias: Identifier? = alias
    @JsonProperty("columns")
    var columns: MutableList<ColumnName> = columns
    @JsonProperty("values")
    var values: MutableList<Expression> = values
    @JsonProperty("whereClause")
    var whereClause: WhereClause? = whereClause
    @JsonProperty("orders")
    var orders: MutableList<SortItem> = orders
    @JsonProperty("limitLines")
    var limitLines: Int? = limitLines
    @JsonProperty("limitOffset")
    var limitOffset: Int? = limitOffset
}

@JsonTypeName("MultipleUpdateStatement")
class MultipleUpdateStatement (
    priority: Priority? = null,
    isIgnore: Boolean,
    columns: MutableList<ColumnName>,
    values: MutableList<Expression>,
    tables: MutableList<TableReferenceClause>,
    whereClause: WhereClause? = null     
): UpdateStatement() {
    @JsonProperty("priority")
    var priority: Priority? = priority
    @JsonProperty("isIgnore")
    var isIgnore: Boolean = isIgnore
    @JsonProperty("columns")
    var columns: MutableList<ColumnName> = columns
    @JsonProperty("values")
    var values: MutableList<Expression> = values
    @JsonProperty("tables")
    var tables: MutableList<TableReferenceClause> = tables
    @JsonProperty("whereClause")
    var whereClause: WhereClause? = whereClause
}

@JsonTypeName("SortItem")
class SortItem (
    expression: Expression,
    sortType: SortType? = null     
): Node() {
    @JsonProperty("expression")
    var expression: Expression = expression
    @JsonProperty("sortType")
    var sortType: SortType? = sortType
}

@JsonTypeName("TableReferenceClause")
open class TableReferenceClause: Node() {

}

@JsonTypeName("NestedTableClause")
class NestedTableClause (
    tables: MutableList<TableReferenceClause>     
): TableReferenceClause() {
    @JsonProperty("tables")
    var tables: MutableList<TableReferenceClause> = tables
}

@JsonTypeName("JoinClause")
class JoinClause (
    joinType: JoinType,
    left: TableReferenceClause? = null,
    right: TableReferenceClause,
    joinCondition: Expression? = null,
    joinColumns: MutableList<ColumnName>     
): TableReferenceClause() {
    @JsonProperty("joinType")
    var joinType: JoinType = joinType
    @JsonProperty("left")
    var left: TableReferenceClause? = left
    @JsonProperty("right")
    var right: TableReferenceClause = right
    @JsonProperty("joinCondition")
    var joinCondition: Expression? = joinCondition
    @JsonProperty("joinColumns")
    var joinColumns: MutableList<ColumnName> = joinColumns
}

@JsonTypeName("SubqueryClause")
class SubqueryClause (
    select: SubqueryExpression,
    presentAs: Boolean,
    alias: Identifier     
): TableReferenceClause() {
    @JsonProperty("select")
    var select: SubqueryExpression = select
    @JsonProperty("presentAs")
    var presentAs: Boolean = presentAs
    @JsonProperty("alias")
    var alias: Identifier = alias
}

@JsonTypeName("TableSource")
class TableSource (
    name: TableName,
    partitions: MutableList<Identifier>,
    presentAs: Boolean,
    alias: Identifier? = null,
    indexHints: MutableList<IndexHintList>     
): TableReferenceClause() {
    @JsonProperty("name")
    var name: TableName = name
    @JsonProperty("partitions")
    var partitions: MutableList<Identifier> = partitions
    @JsonProperty("presentAs")
    var presentAs: Boolean = presentAs
    @JsonProperty("alias")
    var alias: Identifier? = alias
    @JsonProperty("indexHints")
    var indexHints: MutableList<IndexHintList> = indexHints
}

@JsonTypeName("IndexHintList")
class IndexHintList (
    indexHintAction: IndexHintAction,
    indexHintType: IndexHintType? = null,
    keyFormat: SyntaxFormat,
    indexes: MutableList<IndexName>     
): Node() {
    @JsonProperty("indexHintAction")
    var indexHintAction: IndexHintAction = indexHintAction
    @JsonProperty("indexHintType")
    var indexHintType: IndexHintType? = indexHintType
    @JsonProperty("keyFormat")
    var keyFormat: SyntaxFormat = keyFormat
    @JsonProperty("indexes")
    var indexes: MutableList<IndexName> = indexes
}

@JsonTypeName("NestedSelectStatement")
class NestedSelectStatement (
    select: SelectStatement     
): CommonSelectStatement() {
    @JsonProperty("select")
    var select: SelectStatement = select
}

@JsonTypeName("UnionStatement")
class UnionStatement (
    clauses: MutableList<UnionClause>,
    orders: MutableList<SortItem>,
    limitLines: Int? = null,
    limitOffset: Int? = null     
): CommonSelectStatement() {
    @JsonProperty("clauses")
    var clauses: MutableList<UnionClause> = clauses
    @JsonProperty("orders")
    var orders: MutableList<SortItem> = orders
    @JsonProperty("limitLines")
    var limitLines: Int? = limitLines
    @JsonProperty("limitOffset")
    var limitOffset: Int? = limitOffset
}

@JsonTypeName("UnionClause")
class UnionClause (
    statement: CommonSelectStatement,
    unionType: UnionType? = null     
): Node() {
    @JsonProperty("statement")
    var statement: CommonSelectStatement = statement
    @JsonProperty("unionType")
    var unionType: UnionType? = unionType
}

@JsonTypeName("ColumnClause")
class ColumnClause (
    value: Node,
    alias: Identifier? = null,
    presentAs: Boolean? = null     
): Node() {
    @JsonProperty("value")
    var value: Node = value
    @JsonProperty("alias")
    var alias: Identifier? = alias
    @JsonProperty("presentAs")
    var presentAs: Boolean? = presentAs
}

@JsonTypeName("SelectExportClause")
open class SelectExportClause: Node() {

}

@JsonTypeName("ExportList")
class ExportList (
    variables: MutableList<Primitive>     
): SelectExportClause() {
    @JsonProperty("variables")
    var variables: MutableList<Primitive> = variables
}

@JsonTypeName("ExportDumpFile")
class ExportDumpFile (
    fileName: String     
): SelectExportClause() {
    @JsonProperty("fileName")
    var fileName: String = fileName
}

@JsonTypeName("ExportTextFile")
class ExportTextFile (
    fileName: String,
    fileUnloadOptions: MutableList<CommonSimpleOption>     
): SelectExportClause() {
    @JsonProperty("fileName")
    var fileName: String = fileName
    @JsonProperty("fileUnloadOptions")
    var fileUnloadOptions: MutableList<CommonSimpleOption> = fileUnloadOptions
}

@JsonTypeName("FromClause")
class FromClause (
    tables: MutableList<TableReferenceClause>     
): Node() {
    @JsonProperty("tables")
    var tables: MutableList<TableReferenceClause> = tables
}

@JsonTypeName("WhereClause")
class WhereClause (
    value: Expression     
): Node() {
    @JsonProperty("value")
    var value: Expression = value
}

@JsonTypeName("GroupByClause")
class GroupByClause (
    values: MutableList<SortItem>,
    operator: GroupByOperator? = null     
): Node() {
    @JsonProperty("values")
    var values: MutableList<SortItem> = values
    @JsonProperty("operator")
    var operator: GroupByOperator? = operator
}

@JsonTypeName("GroupByOperator")
open class GroupByOperator: Node() {

}

@JsonTypeName("SimpleGroupByOperator")
class SimpleGroupByOperator (
    name: SimpleGroupByOperatorType,
    arguments: MutableList<Expression>     
): GroupByOperator() {
    @JsonProperty("name")
    var name: SimpleGroupByOperatorType = name
    @JsonProperty("arguments")
    var arguments: MutableList<Expression> = arguments
}

@JsonTypeName("SetGroupByOperator")
class SetGroupByOperator (
    arguments: MutableList<Expression>     
): GroupByOperator() {
    @JsonProperty("arguments")
    var arguments: MutableList<Expression> = arguments
}

@JsonTypeName("StartTransactionStatement")
class StartTransactionStatement (
    options: MutableList<TransactionOption>     
): SingleQueryStatement() {
    @JsonProperty("options")
    var options: MutableList<TransactionOption> = options
}

@JsonTypeName("BeginWorkStatement")
class BeginWorkStatement (
    presentWork: Boolean     
): SingleQueryStatement() {
    @JsonProperty("presentWork")
    var presentWork: Boolean = presentWork
}

@JsonTypeName("CommitWorkStatement")
class CommitWorkStatement (
    presentWork: Boolean,
    isChain: Boolean? = null,
    isRelease: Boolean? = null     
): SingleQueryStatement() {
    @JsonProperty("presentWork")
    var presentWork: Boolean = presentWork
    @JsonProperty("isChain")
    var isChain: Boolean? = isChain
    @JsonProperty("isRelease")
    var isRelease: Boolean? = isRelease
}

@JsonTypeName("RollbackWorkStatement")
class RollbackWorkStatement (
    presentWork: Boolean,
    isChain: Boolean? = null,
    isRelease: Boolean? = null     
): SingleQueryStatement() {
    @JsonProperty("presentWork")
    var presentWork: Boolean = presentWork
    @JsonProperty("isChain")
    var isChain: Boolean? = isChain
    @JsonProperty("isRelease")
    var isRelease: Boolean? = isRelease
}

@JsonTypeName("SavepointStatement")
class SavepointStatement (
    savepoint: Identifier     
): SingleQueryStatement() {
    @JsonProperty("savepoint")
    var savepoint: Identifier = savepoint
}

@JsonTypeName("RollbackStatement")
class RollbackStatement (
    presentWork: Boolean,
    presentSavepoint: Boolean,
    savepoint: Identifier     
): SingleQueryStatement() {
    @JsonProperty("presentWork")
    var presentWork: Boolean = presentWork
    @JsonProperty("presentSavepoint")
    var presentSavepoint: Boolean = presentSavepoint
    @JsonProperty("savepoint")
    var savepoint: Identifier = savepoint
}

@JsonTypeName("ReleaseStatement")
class ReleaseStatement (
    savepoint: Identifier     
): SingleQueryStatement() {
    @JsonProperty("savepoint")
    var savepoint: Identifier = savepoint
}

@JsonTypeName("LockTablesStatement")
class LockTablesStatement (
    tables: MutableList<LockTableClause>     
): SingleQueryStatement() {
    @JsonProperty("tables")
    var tables: MutableList<LockTableClause> = tables
}

@JsonTypeName("UnlockTablesStatement")
class UnlockTablesStatement: SingleQueryStatement() {

}

@JsonTypeName("SetAutocommitStatement")
class SetAutocommitStatement (
    value: Boolean     
): SetStatement() {
    @JsonProperty("value")
    var value: Boolean = value
}

@JsonTypeName("SetTransactionStatement")
class SetTransactionStatement (
    context: TransactionContext? = null,
    options: MutableList<TransactionDescriptor>     
): SetStatement() {
    @JsonProperty("context")
    var context: TransactionContext? = context
    @JsonProperty("options")
    var options: MutableList<TransactionDescriptor> = options
}

@JsonTypeName("LockTableClause")
class LockTableClause (
    table: TableName,
    presentAs: Boolean,
    alias: Identifier? = null,
    lockAction: LockTableAction     
): Node() {
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("presentAs")
    var presentAs: Boolean = presentAs
    @JsonProperty("alias")
    var alias: Identifier? = alias
    @JsonProperty("lockAction")
    var lockAction: LockTableAction = lockAction
}

@JsonTypeName("TransactionDescriptor")
class TransactionDescriptor (
    level: TransactionLevel? = null,
    option: TransactionOption? = null     
): Node() {
    @JsonProperty("level")
    var level: TransactionLevel? = level
    @JsonProperty("option")
    var option: TransactionOption? = option
}

@JsonTypeName("ChangeMasterStatement")
class ChangeMasterStatement (
    options: MutableList<CommonSimpleOption>,
    channel: String? = null     
): SingleQueryStatement() {
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
    @JsonProperty("channel")
    var channel: String? = channel
}

@JsonTypeName("ChangeFilterStatement")
class ChangeFilterStatement (
    options: MutableList<CommonSimpleOption>     
): SingleQueryStatement() {
    @JsonProperty("options")
    var options: MutableList<CommonSimpleOption> = options
}

@JsonTypeName("PurgeLogsStatement")
class PurgeLogsStatement (
    purgeFormat: SyntaxFormat,
    file: String? = null,
    time: String? = null     
): SingleQueryStatement() {
    @JsonProperty("purgeFormat")
    var purgeFormat: SyntaxFormat = purgeFormat
    @JsonProperty("file")
    var file: String? = file
    @JsonProperty("time")
    var time: String? = time
}

@JsonTypeName("ResetMasterStatement")
class ResetMasterStatement: SingleQueryStatement() {

}

@JsonTypeName("ResetSlaveStatement")
class ResetSlaveStatement (
    presentAll: Boolean,
    channel: String? = null     
): SingleQueryStatement() {
    @JsonProperty("presentAll")
    var presentAll: Boolean = presentAll
    @JsonProperty("channel")
    var channel: String? = channel
}

@JsonTypeName("StartSlaveStatement")
class StartSlaveStatement (
    threads: MutableList<ThreadType>,
    channel: String? = null,
    untilOptions: MutableList<CommonSimpleOption>,
    connectionOptions: MutableList<CommonSimpleOption>     
): SingleQueryStatement() {
    @JsonProperty("threads")
    var threads: MutableList<ThreadType> = threads
    @JsonProperty("channel")
    var channel: String? = channel
    @JsonProperty("untilOptions")
    var untilOptions: MutableList<CommonSimpleOption> = untilOptions
    @JsonProperty("connectionOptions")
    var connectionOptions: MutableList<CommonSimpleOption> = connectionOptions
}

@JsonTypeName("StopSlaveStatement")
class StopSlaveStatement (
    threads: MutableList<ThreadType>     
): SingleQueryStatement() {
    @JsonProperty("threads")
    var threads: MutableList<ThreadType> = threads
}

@JsonTypeName("StartGroupStatement")
class StartGroupStatement: SingleQueryStatement() {

}

@JsonTypeName("StopGroupStatement")
class StopGroupStatement: SingleQueryStatement() {

}

@JsonTypeName("GTID")
class GTID (
    uuids: MutableList<UUID>,
    value: String? = null     
): Node() {
    @JsonProperty("uuids")
    var uuids: MutableList<UUID> = uuids
    @JsonProperty("value")
    var value: String? = value
}

@JsonTypeName("UUID")
class UUID (
    value: String     
): Node() {
    @JsonProperty("value")
    var value: String = value
}

@JsonTypeName("TablePair")
class TablePair (
    firstTable: TableName,
    secondTable: TableName     
): Node() {
    @JsonProperty("firstTable")
    var firstTable: TableName = firstTable
    @JsonProperty("secondTable")
    var secondTable: TableName = secondTable
}

@JsonTypeName("XAStartTransactionStatement")
class XAStartTransactionStatement (
    startFormat: SyntaxFormat,
    name: XIDName,
    actionFormat: SyntaxFormat? = null     
): SingleQueryStatement() {
    @JsonProperty("startFormat")
    var startFormat: SyntaxFormat = startFormat
    @JsonProperty("name")
    var name: XIDName = name
    @JsonProperty("actionFormat")
    var actionFormat: SyntaxFormat? = actionFormat
}

@JsonTypeName("XAEndTransactionStatement")
class XAEndTransactionStatement (
    name: XIDName,
    suspendFormat: SyntaxFormat? = null     
): SingleQueryStatement() {
    @JsonProperty("name")
    var name: XIDName = name
    @JsonProperty("suspendFormat")
    var suspendFormat: SyntaxFormat? = suspendFormat
}

@JsonTypeName("XAPrepareStatement")
class XAPrepareStatement (
    name: XIDName     
): SingleQueryStatement() {
    @JsonProperty("name")
    var name: XIDName = name
}

@JsonTypeName("XACommitStatement")
class XACommitStatement (
    name: XIDName,
    phaseFormat: SyntaxFormat? = null     
): SingleQueryStatement() {
    @JsonProperty("name")
    var name: XIDName = name
    @JsonProperty("phaseFormat")
    var phaseFormat: SyntaxFormat? = phaseFormat
}

@JsonTypeName("XARollbackStatement")
class XARollbackStatement (
    name: XIDName     
): SingleQueryStatement() {
    @JsonProperty("name")
    var name: XIDName = name
}

@JsonTypeName("XARecoverStatement")
class XARecoverStatement (
    name: XIDName? = null     
): SingleQueryStatement() {
    @JsonProperty("name")
    var name: XIDName? = name
}

@JsonTypeName("PrepareStatement")
class PrepareStatement (
    id: Identifier,
    query: String? = null,
    variable: Variable? = null     
): SingleQueryStatement() {
    @JsonProperty("id")
    var id: Identifier = id
    @JsonProperty("query")
    var query: String? = query
    @JsonProperty("variable")
    var variable: Variable? = variable
}

@JsonTypeName("ExecuteStatement")
class ExecuteStatement (
    id: Identifier,
    variables: MutableList<Variable>     
): SingleQueryStatement() {
    @JsonProperty("id")
    var id: Identifier = id
    @JsonProperty("variables")
    var variables: MutableList<Variable> = variables
}

@JsonTypeName("DeallocateStatement")
class DeallocateStatement (
    deallocateFormat: SyntaxFormat,
    id: Identifier     
): SingleQueryStatement() {
    @JsonProperty("deallocateFormat")
    var deallocateFormat: SyntaxFormat = deallocateFormat
    @JsonProperty("id")
    var id: Identifier = id
}

@JsonTypeName("RoutineStatement")
open class RoutineStatement: CommonStatement() {

}

@JsonTypeName("BlockQueryStatement")
class BlockQueryStatement (
    body: MutableList<CommonStatement>,
    label: Identifier? = null     
): Statement() {
    @JsonProperty("body")
    var body: MutableList<CommonStatement> = body
    @JsonProperty("label")
    var label: Identifier? = label
}

@JsonTypeName("CaseStatement")
class CaseStatement (
    test: Expression? = null,
    alternatives: MutableList<ConditionChoiceOption>,
    elseAlternatives: MutableList<Statement>     
): RoutineStatement() {
    @JsonProperty("test")
    var test: Expression? = test
    @JsonProperty("alternatives")
    var alternatives: MutableList<ConditionChoiceOption> = alternatives
    @JsonProperty("elseAlternatives")
    var elseAlternatives: MutableList<Statement> = elseAlternatives
}

@JsonTypeName("IfStatement")
class IfStatement (
    test: Expression,
    statements: MutableList<Statement>,
    alternatives: MutableList<ConditionChoiceOption>,
    elseAlternatives: MutableList<Statement>     
): RoutineStatement() {
    @JsonProperty("test")
    var test: Expression = test
    @JsonProperty("statements")
    var statements: MutableList<Statement> = statements
    @JsonProperty("alternatives")
    var alternatives: MutableList<ConditionChoiceOption> = alternatives
    @JsonProperty("elseAlternatives")
    var elseAlternatives: MutableList<Statement> = elseAlternatives
}

@JsonTypeName("IterateStatement")
class IterateStatement (
    label: Identifier     
): RoutineStatement() {
    @JsonProperty("label")
    var label: Identifier = label
}

@JsonTypeName("LeaveStatement")
class LeaveStatement (
    label: Identifier     
): RoutineStatement() {
    @JsonProperty("label")
    var label: Identifier = label
}

@JsonTypeName("LoopStatement")
class LoopStatement (
    label: Identifier,
    statements: MutableList<Statement>     
): RoutineStatement() {
    @JsonProperty("label")
    var label: Identifier = label
    @JsonProperty("statements")
    var statements: MutableList<Statement> = statements
}

@JsonTypeName("RepeatStatement")
class RepeatStatement (
    test: Expression,
    label: Identifier,
    statements: MutableList<Statement>     
): RoutineStatement() {
    @JsonProperty("test")
    var test: Expression = test
    @JsonProperty("label")
    var label: Identifier = label
    @JsonProperty("statements")
    var statements: MutableList<Statement> = statements
}

@JsonTypeName("ReturnStatement")
class ReturnStatement (
    value: Expression     
): RoutineStatement() {
    @JsonProperty("value")
    var value: Expression = value
}

@JsonTypeName("WhileStatement")
class WhileStatement (
    test: Expression,
    label: Identifier,
    statements: MutableList<Statement>     
): RoutineStatement() {
    @JsonProperty("test")
    var test: Expression = test
    @JsonProperty("label")
    var label: Identifier = label
    @JsonProperty("statements")
    var statements: MutableList<Statement> = statements
}

@JsonTypeName("OpenCursorStatement")
class OpenCursorStatement (
    name: Identifier     
): RoutineStatement() {
    @JsonProperty("name")
    var name: Identifier = name
}

@JsonTypeName("FetchCursorStatement")
class FetchCursorStatement (
    name: Identifier,
    variables: MutableList<Identifier>,
    presentFrom: Boolean,
    presentNext: Boolean     
): RoutineStatement() {
    @JsonProperty("name")
    var name: Identifier = name
    @JsonProperty("variables")
    var variables: MutableList<Identifier> = variables
    @JsonProperty("presentFrom")
    var presentFrom: Boolean = presentFrom
    @JsonProperty("presentNext")
    var presentNext: Boolean = presentNext
}

@JsonTypeName("CloseCursorStatement")
class CloseCursorStatement (
    name: Identifier     
): RoutineStatement() {
    @JsonProperty("name")
    var name: Identifier = name
}

@JsonTypeName("StatementDeclaration")
open class StatementDeclaration: RoutineStatement() {

}

@JsonTypeName("VariableDeclaration")
class VariableDeclaration (
    variables: MutableList<Identifier>,
    dataType: DataTypeClause,
    defaultValue: Literal? = null     
): StatementDeclaration() {
    @JsonProperty("variables")
    var variables: MutableList<Identifier> = variables
    @JsonProperty("dataType")
    var dataType: DataTypeClause = dataType
    @JsonProperty("defaultValue")
    var defaultValue: Literal? = defaultValue
}

@JsonTypeName("ConditionDeclaration")
class ConditionDeclaration (
    name: Identifier,
    errorCode: Int? = null,
    sqlState: String? = null,
    presentValue: Boolean? = null     
): StatementDeclaration() {
    @JsonProperty("name")
    var name: Identifier = name
    @JsonProperty("errorCode")
    var errorCode: Int? = errorCode
    @JsonProperty("sqlState")
    var sqlState: String? = sqlState
    @JsonProperty("presentValue")
    var presentValue: Boolean? = presentValue
}

@JsonTypeName("CursorDeclaration")
class CursorDeclaration (
    cursor: Identifier,
    select: CommonSelectStatement     
): StatementDeclaration() {
    @JsonProperty("cursor")
    var cursor: Identifier = cursor
    @JsonProperty("select")
    var select: CommonSelectStatement = select
}

@JsonTypeName("HandlerDeclaration")
class HandlerDeclaration (
    action: HandlerAction,
    conditions: MutableList<HandlerCondition>,
    statement: Statement     
): StatementDeclaration() {
    @JsonProperty("action")
    var action: HandlerAction = action
    @JsonProperty("conditions")
    var conditions: MutableList<HandlerCondition> = conditions
    @JsonProperty("statement")
    var statement: Statement = statement
}

@JsonTypeName("HandlerCondition")
open class HandlerCondition: Node() {

}

@JsonTypeName("HandlerConditionCode")
class HandlerConditionCode (
    value: Int     
): HandlerCondition() {
    @JsonProperty("value")
    var value: Int = value
}

@JsonTypeName("HandlerConditionSQLState")
class HandlerConditionSQLState (
    value: String,
    presentValue: Boolean     
): HandlerCondition() {
    @JsonProperty("value")
    var value: String = value
    @JsonProperty("presentValue")
    var presentValue: Boolean = presentValue
}

@JsonTypeName("HandlerConditionName")
class HandlerConditionName (
    value: String     
): HandlerCondition() {
    @JsonProperty("value")
    var value: String = value
}

@JsonTypeName("HandlerConditionWarning")
class HandlerConditionWarning: HandlerCondition() {

}

@JsonTypeName("HandlerConditionNotFound")
class HandlerConditionNotFound: HandlerCondition() {

}

@JsonTypeName("HandlerConditionException")
class HandlerConditionException: HandlerCondition() {

}

@JsonTypeName("ConditionChoiceOption")
class ConditionChoiceOption (
    test: Expression,
    statements: MutableList<Statement>     
): Node() {
    @JsonProperty("test")
    var test: Expression = test
    @JsonProperty("statements")
    var statements: MutableList<Statement> = statements
}

@JsonTypeName("AlterUserShortStatement")
class AlterUserShortStatement (
    users: MutableList<UserName>,
    passwordOptions: MutableList<PasswordExpirationClause>     
): SingleQueryStatement() {
    @JsonProperty("users")
    var users: MutableList<UserName> = users
    @JsonProperty("passwordOptions")
    var passwordOptions: MutableList<PasswordExpirationClause> = passwordOptions
}

@JsonTypeName("AlterUserFullStatement")
class AlterUserFullStatement (
    ifExists: Boolean,
    userAuthOptions: MutableList<UserClause>,
    tlsOptions: MutableList<TLSOptionClause>,
    resourseOptions: MutableList<CommonSimpleOption>,
    passwordOptions: MutableList<PasswordExpirationClause>,
    isLock: Boolean? = null     
): SingleQueryStatement() {
    @JsonProperty("ifExists")
    var ifExists: Boolean = ifExists
    @JsonProperty("userAuthOptions")
    var userAuthOptions: MutableList<UserClause> = userAuthOptions
    @JsonProperty("tlsOptions")
    var tlsOptions: MutableList<TLSOptionClause> = tlsOptions
    @JsonProperty("resourseOptions")
    var resourseOptions: MutableList<CommonSimpleOption> = resourseOptions
    @JsonProperty("passwordOptions")
    var passwordOptions: MutableList<PasswordExpirationClause> = passwordOptions
    @JsonProperty("isLock")
    var isLock: Boolean? = isLock
}

@JsonTypeName("CreateUserStatement")
class CreateUserStatement (
    ifExists: Boolean,
    userAuthOptions: MutableList<UserClause>,
    tlsOptions: MutableList<TLSOptionClause>,
    resourseOptions: MutableList<CommonSimpleOption>,
    passwordOptions: MutableList<PasswordExpirationClause>,
    isLock: Boolean? = null     
): SingleQueryStatement() {
    @JsonProperty("ifExists")
    var ifExists: Boolean = ifExists
    @JsonProperty("userAuthOptions")
    var userAuthOptions: MutableList<UserClause> = userAuthOptions
    @JsonProperty("tlsOptions")
    var tlsOptions: MutableList<TLSOptionClause> = tlsOptions
    @JsonProperty("resourseOptions")
    var resourseOptions: MutableList<CommonSimpleOption> = resourseOptions
    @JsonProperty("passwordOptions")
    var passwordOptions: MutableList<PasswordExpirationClause> = passwordOptions
    @JsonProperty("isLock")
    var isLock: Boolean? = isLock
}

@JsonTypeName("DropUserStatement")
class DropUserStatement (
    user: MutableList<UserName>,
    ifExists: Boolean     
): SingleQueryStatement() {
    @JsonProperty("user")
    var user: MutableList<UserName> = user
    @JsonProperty("ifExists")
    var ifExists: Boolean = ifExists
}

@JsonTypeName("GrantStatement")
class GrantStatement (
    privileges: MutableList<PrivilegeClause>,
    objectType: PrivilegeObjectType,
    userAuthOptions: MutableList<UserClause>,
    tlsOptions: MutableList<TLSOptionClause>,
    resourseOptions: MutableList<CommonSimpleOption>,
    isGrantOption: Boolean,
    level: PrivilegeLevelClause     
): SingleQueryStatement() {
    @JsonProperty("privileges")
    var privileges: MutableList<PrivilegeClause> = privileges
    @JsonProperty("objectType")
    var objectType: PrivilegeObjectType = objectType
    @JsonProperty("userAuthOptions")
    var userAuthOptions: MutableList<UserClause> = userAuthOptions
    @JsonProperty("tlsOptions")
    var tlsOptions: MutableList<TLSOptionClause> = tlsOptions
    @JsonProperty("resourseOptions")
    var resourseOptions: MutableList<CommonSimpleOption> = resourseOptions
    @JsonProperty("isGrantOption")
    var isGrantOption: Boolean = isGrantOption
    @JsonProperty("level")
    var level: PrivilegeLevelClause = level
}

@JsonTypeName("GrantProxyStatement")
class GrantProxyStatement (
    from: UserName,
    to: MutableList<UserName>,
    isGrantOption: Boolean     
): SingleQueryStatement() {
    @JsonProperty("from")
    var from: UserName = from
    @JsonProperty("to")
    var to: MutableList<UserName> = to
    @JsonProperty("isGrantOption")
    var isGrantOption: Boolean = isGrantOption
}

@JsonTypeName("RenameUserStatement")
class RenameUserStatement (
    clauses: MutableList<RenameUserClause>     
): SingleQueryStatement() {
    @JsonProperty("clauses")
    var clauses: MutableList<RenameUserClause> = clauses
}

@JsonTypeName("RenameUserClause")
class RenameUserClause (
    from: UserName,
    to: UserName     
): Node() {
    @JsonProperty("from")
    var from: UserName = from
    @JsonProperty("to")
    var to: UserName = to
}

@JsonTypeName("RevokeStatement")
class RevokeStatement (
    privileges: MutableList<PrivilegeClause>,
    objectType: PrivilegeObjectType,
    level: PrivilegeLevelClause,
    users: MutableList<UserName>     
): SingleQueryStatement() {
    @JsonProperty("privileges")
    var privileges: MutableList<PrivilegeClause> = privileges
    @JsonProperty("objectType")
    var objectType: PrivilegeObjectType = objectType
    @JsonProperty("level")
    var level: PrivilegeLevelClause = level
    @JsonProperty("users")
    var users: MutableList<UserName> = users
}

@JsonTypeName("FullRevokeStatement")
class FullRevokeStatement (
    users: MutableList<UserName>,
    presentPrivileges: Boolean     
): SingleQueryStatement() {
    @JsonProperty("users")
    var users: MutableList<UserName> = users
    @JsonProperty("presentPrivileges")
    var presentPrivileges: Boolean = presentPrivileges
}

@JsonTypeName("RevokeProxyStatement")
class RevokeProxyStatement (
    on: UserName,
    from: MutableList<UserName>     
): SingleQueryStatement() {
    @JsonProperty("on")
    var on: UserName = on
    @JsonProperty("from")
    var from: MutableList<UserName> = from
}

@JsonTypeName("SetPasswordStatement")
class SetPasswordStatement (
    user: UserName? = null,
    value: String? = null,
    expression: PasswordFunctionCall? = null     
): SetStatement() {
    @JsonProperty("user")
    var user: UserName? = user
    @JsonProperty("value")
    var value: String? = value
    @JsonProperty("expression")
    var expression: PasswordFunctionCall? = expression
}

@JsonTypeName("PasswordExpirationClause")
class PasswordExpirationClause (
    expireType: PasswordExpirationType? = null,
    expireValue: Int     
): Node() {
    @JsonProperty("expireType")
    var expireType: PasswordExpirationType? = expireType
    @JsonProperty("expireValue")
    var expireValue: Int = expireValue
}

@JsonTypeName("UserClause")
class UserClause (
    user: UserName,
    passwordFormat: SyntaxFormat,
    hashText: String? = null,
    plainText: String? = null,
    authPlugin: AuthPlugin? = null     
): Node() {
    @JsonProperty("user")
    var user: UserName = user
    @JsonProperty("passwordFormat")
    var passwordFormat: SyntaxFormat = passwordFormat
    @JsonProperty("hashText")
    var hashText: String? = hashText
    @JsonProperty("plainText")
    var plainText: String? = plainText
    @JsonProperty("authPlugin")
    var authPlugin: AuthPlugin? = authPlugin
}

@JsonTypeName("TLSOptionClause")
class TLSOptionClause (
    option: TLSOptionName,
    value: String? = null     
): Node() {
    @JsonProperty("option")
    var option: TLSOptionName = option
    @JsonProperty("value")
    var value: String? = value
}

@JsonTypeName("PrivilegeClause")
class PrivilegeClause (
    privilege: PrivilegeName,
    columns: MutableList<Identifier>     
): Node() {
    @JsonProperty("privilege")
    var privilege: PrivilegeName = privilege
    @JsonProperty("columns")
    var columns: MutableList<Identifier> = columns
}

@JsonTypeName("PrivilegeLevelClause")
class PrivilegeLevelClause (
    level: PrivilegeLevel,
    schema: SchemaName? = null,
    table: TableName? = null,
    routine: FullName? = null     
): Node() {
    @JsonProperty("level")
    var level: PrivilegeLevel = level
    @JsonProperty("schema")
    var schema: SchemaName? = schema
    @JsonProperty("table")
    var table: TableName? = table
    @JsonProperty("routine")
    var routine: FullName? = routine
}

@JsonTypeName("AnalyzeTableStatement")
class AnalyzeTableStatement (
    tables: MutableList<TableName>,
    actionOption: SyntaxFormat     
): SingleQueryStatement() {
    @JsonProperty("tables")
    var tables: MutableList<TableName> = tables
    @JsonProperty("actionOption")
    var actionOption: SyntaxFormat = actionOption
}

@JsonTypeName("CheckTableStatement")
class CheckTableStatement (
    tables: MutableList<TableName>,
    options: MutableList<CheckTableOption>     
): SingleQueryStatement() {
    @JsonProperty("tables")
    var tables: MutableList<TableName> = tables
    @JsonProperty("options")
    var options: MutableList<CheckTableOption> = options
}

@JsonTypeName("ChecksumTableStatement")
class ChecksumTableStatement (
    tables: MutableList<TableName>,
    actionOption: SyntaxFormat? = null     
): SingleQueryStatement() {
    @JsonProperty("tables")
    var tables: MutableList<TableName> = tables
    @JsonProperty("actionOption")
    var actionOption: SyntaxFormat? = actionOption
}

@JsonTypeName("OptimizeTableStatement")
class OptimizeTableStatement (
    tables: MutableList<TableName>,
    actionOption: SyntaxFormat? = null     
): SingleQueryStatement() {
    @JsonProperty("tables")
    var tables: MutableList<TableName> = tables
    @JsonProperty("actionOption")
    var actionOption: SyntaxFormat? = actionOption
}

@JsonTypeName("RepairTableStatement")
class RepairTableStatement (
    tables: MutableList<TableName>,
    actionOption: SyntaxFormat? = null,
    isQuick: Boolean,
    isExtended: Boolean,
    isUseFrm: Boolean     
): SingleQueryStatement() {
    @JsonProperty("tables")
    var tables: MutableList<TableName> = tables
    @JsonProperty("actionOption")
    var actionOption: SyntaxFormat? = actionOption
    @JsonProperty("isQuick")
    var isQuick: Boolean = isQuick
    @JsonProperty("isExtended")
    var isExtended: Boolean = isExtended
    @JsonProperty("isUseFrm")
    var isUseFrm: Boolean = isUseFrm
}

@JsonTypeName("CreateUDFunctionStatement")
class CreateUDFunctionStatement (
    presentAggregate: Boolean,
    id: Identifier,
    return_: ReturnDataType,
    name: String     
): SingleQueryStatement() {
    @JsonProperty("presentAggregate")
    var presentAggregate: Boolean = presentAggregate
    @JsonProperty("id")
    var id: Identifier = id
    @JsonProperty("return")
    var return_: ReturnDataType = return_
    @JsonProperty("name")
    var name: String = name
}

@JsonTypeName("InstallPluginStatement")
class InstallPluginStatement (
    id: Identifier,
    name: String     
): SingleQueryStatement() {
    @JsonProperty("id")
    var id: Identifier = id
    @JsonProperty("name")
    var name: String = name
}

@JsonTypeName("UninstallPluginStatement")
class UninstallPluginStatement (
    id: Identifier     
): SingleQueryStatement() {
    @JsonProperty("id")
    var id: Identifier = id
}

@JsonTypeName("SetStatement")
open class SetStatement: SingleQueryStatement() {

}

@JsonTypeName("SetVariableStatement")
class SetVariableStatement (
    variables: MutableList<Variable>,
    expressions: MutableList<Expression>     
): SetStatement() {
    @JsonProperty("variables")
    var variables: MutableList<Variable> = variables
    @JsonProperty("expressions")
    var expressions: MutableList<Expression> = expressions
}

@JsonTypeName("SetCharsetStatement")
class SetCharsetStatement (
    charSetName: CharSet? = null,
    charsetFormat: SyntaxFormat,
    isNameDefault: Boolean     
): SetStatement() {
    @JsonProperty("charSetName")
    var charSetName: CharSet? = charSetName
    @JsonProperty("charsetFormat")
    var charsetFormat: SyntaxFormat = charsetFormat
    @JsonProperty("isNameDefault")
    var isNameDefault: Boolean = isNameDefault
}

@JsonTypeName("SetNamesStatement")
class SetNamesStatement (
    charSetName: CharSet? = null,
    collationName: String? = null,
    isNameDefault: Boolean     
): SetStatement() {
    @JsonProperty("charSetName")
    var charSetName: CharSet? = charSetName
    @JsonProperty("collationName")
    var collationName: String? = collationName
    @JsonProperty("isNameDefault")
    var isNameDefault: Boolean = isNameDefault
}

@JsonTypeName("ShowStatement")
open class ShowStatement: SingleQueryStatement() {

}

@JsonTypeName("ShowLogsStatement")
class ShowLogsStatement (
    logTypeFormat: SyntaxFormat     
): ShowStatement() {
    @JsonProperty("logTypeFormat")
    var logTypeFormat: SyntaxFormat = logTypeFormat
}

@JsonTypeName("ShowLogEventsStatement")
class ShowLogEventsStatement (
    logTypeFormat: SyntaxFormat,
    filename: String? = null,
    fromPosition: Int? = null,
    limitOffset: Int? = null,
    limitCount: Int? = null     
): ShowStatement() {
    @JsonProperty("logTypeFormat")
    var logTypeFormat: SyntaxFormat = logTypeFormat
    @JsonProperty("filename")
    var filename: String? = filename
    @JsonProperty("fromPosition")
    var fromPosition: Int? = fromPosition
    @JsonProperty("limitOffset")
    var limitOffset: Int? = limitOffset
    @JsonProperty("limitCount")
    var limitCount: Int? = limitCount
}

@JsonTypeName("ShowEntityStatement")
class ShowEntityStatement (
    entity: CommonEntity,
    filter: ShowFilterClause? = null,
    schema: SchemaName? = null,
    schemaFormat: SyntaxFormat? = null     
): ShowStatement() {
    @JsonProperty("entity")
    var entity: CommonEntity = entity
    @JsonProperty("filter")
    var filter: ShowFilterClause? = filter
    @JsonProperty("schema")
    var schema: SchemaName? = schema
    @JsonProperty("schemaFormat")
    var schemaFormat: SyntaxFormat? = schemaFormat
}

@JsonTypeName("ShowColumnsStatement")
class ShowColumnsStatement (
    presentFull: Boolean,
    columnFormat: SyntaxFormat,
    tableFormat: SyntaxFormat,
    table: TableName,
    schemaFormat: SyntaxFormat? = null,
    schema: SchemaName? = null,
    filter: ShowFilterClause? = null     
): ShowStatement() {
    @JsonProperty("presentFull")
    var presentFull: Boolean = presentFull
    @JsonProperty("columnFormat")
    var columnFormat: SyntaxFormat = columnFormat
    @JsonProperty("tableFormat")
    var tableFormat: SyntaxFormat = tableFormat
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("schemaFormat")
    var schemaFormat: SyntaxFormat? = schemaFormat
    @JsonProperty("schema")
    var schema: SchemaName? = schema
    @JsonProperty("filter")
    var filter: ShowFilterClause? = filter
}

@JsonTypeName("ShowCreateSchemaStatement")
class ShowCreateSchemaStatement (
    schemaFormat: SyntaxFormat? = null,
    ifNotExists: Boolean,
    schema: SchemaName? = null     
): ShowStatement() {
    @JsonProperty("schemaFormat")
    var schemaFormat: SyntaxFormat? = schemaFormat
    @JsonProperty("ifNotExists")
    var ifNotExists: Boolean = ifNotExists
    @JsonProperty("schema")
    var schema: SchemaName? = schema
}

@JsonTypeName("ShowCreateNamedEntityStatement")
class ShowCreateNamedEntityStatement (
    entity: NamedEntity,
    entityName: FullName     
): ShowStatement() {
    @JsonProperty("entity")
    var entity: NamedEntity = entity
    @JsonProperty("entityName")
    var entityName: FullName = entityName
}

@JsonTypeName("ShowCreateUserStatement")
class ShowCreateUserStatement (
    user: UserName     
): ShowStatement() {
    @JsonProperty("user")
    var user: UserName = user
}

@JsonTypeName("ShowEngineStatement")
class ShowEngineStatement (
    engine: String,
    engineFormat: SyntaxFormat     
): ShowStatement() {
    @JsonProperty("engine")
    var engine: String = engine
    @JsonProperty("engineFormat")
    var engineFormat: SyntaxFormat = engineFormat
}

@JsonTypeName("ShowInfoStatement")
class ShowInfoStatement (
    entity: CommonEntity     
): ShowStatement() {
    @JsonProperty("entity")
    var entity: CommonEntity = entity
}

@JsonTypeName("ShowErrorsStatement")
class ShowErrorsStatement (
    errorFormat: SyntaxFormat,
    limitOffset: Int? = null,
    limitCount: Int? = null     
): ShowStatement() {
    @JsonProperty("errorFormat")
    var errorFormat: SyntaxFormat = errorFormat
    @JsonProperty("limitOffset")
    var limitOffset: Int? = limitOffset
    @JsonProperty("limitCount")
    var limitCount: Int? = limitCount
}

@JsonTypeName("ShowCountErrorsStatement")
class ShowCountErrorsStatement (
    errorFormat: SyntaxFormat     
): ShowStatement() {
    @JsonProperty("errorFormat")
    var errorFormat: SyntaxFormat = errorFormat
}

@JsonTypeName("ShowRoutineCodeStatement")
class ShowRoutineCodeStatement (
    routine: NamedEntity,
    routineName: FullName     
): ShowStatement() {
    @JsonProperty("routine")
    var routine: NamedEntity = routine
    @JsonProperty("routineName")
    var routineName: FullName = routineName
}

@JsonTypeName("ShowGrantsStatement")
class ShowGrantsStatement (
    user: UserName? = null     
): ShowStatement() {
    @JsonProperty("user")
    var user: UserName? = user
}

@JsonTypeName("ShowIndexesStatement")
class ShowIndexesStatement (
    entity: CommonEntity,
    tableFormat: SyntaxFormat,
    table: TableName,
    schemaFormat: SyntaxFormat? = null,
    schema: SchemaName? = null,
    whereClause: WhereClause? = null     
): ShowStatement() {
    @JsonProperty("entity")
    var entity: CommonEntity = entity
    @JsonProperty("tableFormat")
    var tableFormat: SyntaxFormat = tableFormat
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("schemaFormat")
    var schemaFormat: SyntaxFormat? = schemaFormat
    @JsonProperty("schema")
    var schema: SchemaName? = schema
    @JsonProperty("whereClause")
    var whereClause: WhereClause? = whereClause
}

@JsonTypeName("ShowOpenTablesStatement")
class ShowOpenTablesStatement (
    schemaFormat: SyntaxFormat? = null,
    schema: SchemaName? = null,
    filter: ShowFilterClause? = null     
): ShowStatement() {
    @JsonProperty("schemaFormat")
    var schemaFormat: SyntaxFormat? = schemaFormat
    @JsonProperty("schema")
    var schema: SchemaName? = schema
    @JsonProperty("filter")
    var filter: ShowFilterClause? = filter
}

@JsonTypeName("ShowProfileStatement")
class ShowProfileStatement (
    profileTypes: MutableList<ProfileType>,
    queryCount: Int? = null,
    limitOffset: Int? = null,
    limitCount: Int? = null     
): ShowStatement() {
    @JsonProperty("profileTypes")
    var profileTypes: MutableList<ProfileType> = profileTypes
    @JsonProperty("queryCount")
    var queryCount: Int? = queryCount
    @JsonProperty("limitOffset")
    var limitOffset: Int? = limitOffset
    @JsonProperty("limitCount")
    var limitCount: Int? = limitCount
}

@JsonTypeName("ShowSlaveStatement")
class ShowSlaveStatement (
    channel: String? = null     
): ShowStatement() {
    @JsonProperty("channel")
    var channel: String? = channel
}

@JsonTypeName("ShowFilterClause")
class ShowFilterClause (
    expression: Expression? = null,
    pattern: StringLiteral? = null     
): Node() {
    @JsonProperty("expression")
    var expression: Expression? = expression
    @JsonProperty("pattern")
    var pattern: StringLiteral? = pattern
}

@JsonTypeName("BinlogStatement")
class BinlogStatement (
    filename: String     
): SingleQueryStatement() {
    @JsonProperty("filename")
    var filename: String = filename
}

@JsonTypeName("CacheIndexStatement")
class CacheIndexStatement (
    tableIndexes: MutableList<TableIndexClause>,
    partitions: MutableList<Identifier>,
    isAll: Boolean,
    schema: SchemaName     
): SingleQueryStatement() {
    @JsonProperty("tableIndexes")
    var tableIndexes: MutableList<TableIndexClause> = tableIndexes
    @JsonProperty("partitions")
    var partitions: MutableList<Identifier> = partitions
    @JsonProperty("isAll")
    var isAll: Boolean = isAll
    @JsonProperty("schema")
    var schema: SchemaName = schema
}

@JsonTypeName("FlushStatement")
class FlushStatement (
    flushFormat: SyntaxFormat? = null,
    options: MutableList<FlushOption>     
): SingleQueryStatement() {
    @JsonProperty("flushFormat")
    var flushFormat: SyntaxFormat? = flushFormat
    @JsonProperty("options")
    var options: MutableList<FlushOption> = options
}

@JsonTypeName("KillStatement")
class KillStatement (
    connectionFormat: SyntaxFormat? = null,
    connections: MutableList<Int>     
): SingleQueryStatement() {
    @JsonProperty("connectionFormat")
    var connectionFormat: SyntaxFormat? = connectionFormat
    @JsonProperty("connections")
    var connections: MutableList<Int> = connections
}

@JsonTypeName("LoadIndexStatement")
class LoadIndexStatement (
    tableIndexes: MutableList<TableIndexClause>     
): SingleQueryStatement() {
    @JsonProperty("tableIndexes")
    var tableIndexes: MutableList<TableIndexClause> = tableIndexes
}

@JsonTypeName("ResetStatement")
class ResetStatement: SingleQueryStatement() {

}

@JsonTypeName("ShutdownStatement")
class ShutdownStatement: SingleQueryStatement() {

}

@JsonTypeName("TableIndexClause")
class TableIndexClause (
    table: TableName,
    indexFormat: SyntaxFormat? = null,
    indexes: MutableList<Identifier>,
    partitions: MutableList<Identifier>,
    isAllPartitiions: Boolean? = null,
    isIgnoreLeaves: Boolean? = null     
): Node() {
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("indexFormat")
    var indexFormat: SyntaxFormat? = indexFormat
    @JsonProperty("indexes")
    var indexes: MutableList<Identifier> = indexes
    @JsonProperty("partitions")
    var partitions: MutableList<Identifier> = partitions
    @JsonProperty("isAllPartitiions")
    var isAllPartitiions: Boolean? = isAllPartitiions
    @JsonProperty("isIgnoreLeaves")
    var isIgnoreLeaves: Boolean? = isIgnoreLeaves
}

@JsonTypeName("FlushOptionClause")
open class FlushOptionClause: Node() {

}

@JsonTypeName("SimpleFlushOptionClause")
class SimpleFlushOptionClause (
    option: FlushOption     
): FlushOptionClause() {
    @JsonProperty("option")
    var option: FlushOption = option
}

@JsonTypeName("ChannelFlushOptionClause")
class ChannelFlushOptionClause (
    channel: String     
): FlushOptionClause() {
    @JsonProperty("channel")
    var channel: String = channel
}

@JsonTypeName("TablesFlushOptionClause")
class TablesFlushOptionClause (
    tables: MutableList<TableName>     
): FlushOptionClause() {
    @JsonProperty("tables")
    var tables: MutableList<TableName> = tables
}

@JsonTypeName("TableDescription")
class TableDescription (
    describeKeyword: DescriptionStatementType,
    table: TableName,
    column: ColumnName? = null,
    columnWildcard: String? = null     
): SingleQueryStatement() {
    @JsonProperty("describeKeyword")
    var describeKeyword: DescriptionStatementType = describeKeyword
    @JsonProperty("table")
    var table: TableName = table
    @JsonProperty("column")
    var column: ColumnName? = column
    @JsonProperty("columnWildcard")
    var columnWildcard: String? = columnWildcard
}

@JsonTypeName("FullTableDescription")
class FullTableDescription (
    describeKeyword: DescriptionStatementType,
    describeFormat: FormatDescriptionClause? = null,
    describeObject: ObjectDescriptionClause     
): SingleQueryStatement() {
    @JsonProperty("describeKeyword")
    var describeKeyword: DescriptionStatementType = describeKeyword
    @JsonProperty("describeFormat")
    var describeFormat: FormatDescriptionClause? = describeFormat
    @JsonProperty("describeObject")
    var describeObject: ObjectDescriptionClause = describeObject
}

@JsonTypeName("HelpStatement")
class HelpStatement (
    question: String     
): SingleQueryStatement() {
    @JsonProperty("question")
    var question: String = question
}

@JsonTypeName("UseStatement")
class UseStatement (
    schema: SchemaName     
): SingleQueryStatement() {
    @JsonProperty("schema")
    var schema: SchemaName = schema
}

@JsonTypeName("FormatDescriptionClause")
class FormatDescriptionClause (
    formatObject: FormatDescriptionObject,
    formatValue: DescribeFormatValue     
): Node() {
    @JsonProperty("formatObject")
    var formatObject: FormatDescriptionObject = formatObject
    @JsonProperty("formatValue")
    var formatValue: DescribeFormatValue = formatValue
}

@JsonTypeName("ObjectDescriptionClause")
class ObjectDescriptionClause (
    statement: SingleQueryStatement? = null,
    connectionId: Identifier? = null     
): Node() {
    @JsonProperty("statement")
    var statement: SingleQueryStatement? = statement
    @JsonProperty("connectionId")
    var connectionId: Identifier? = connectionId
}

@JsonTypeName("FullName")
open class FullName: Node() {

}

@JsonTypeName("TableName")
class TableName (
    db: Identifier? = null,
    schema: Identifier? = null,
    table: Identifier     
): FullName() {
    @JsonProperty("db")
    var db: Identifier? = db
    @JsonProperty("schema")
    var schema: Identifier? = schema
    @JsonProperty("table")
    var table: Identifier = table
}

@JsonTypeName("ColumnName")
class ColumnName (
    db: Identifier? = null,
    schema: Identifier? = null,
    table: Identifier? = null,
    column: Node     
): Primitive() {
    @JsonProperty("db")
    var db: Identifier? = db
    @JsonProperty("schema")
    var schema: Identifier? = schema
    @JsonProperty("table")
    var table: Identifier? = table
    @JsonProperty("column")
    var column: Node = column
}

@JsonTypeName("IndexColumnNameClause")
class IndexColumnNameClause (
    columnName: Identifier,
    length: Int? = null,
    sortType: SortType? = null     
): Node() {
    @JsonProperty("columnName")
    var columnName: Identifier = columnName
    @JsonProperty("length")
    var length: Int? = length
    @JsonProperty("sortType")
    var sortType: SortType? = sortType
}

@JsonTypeName("UserName")
class UserName (
    name: String,
    host: String     
): Node() {
    @JsonProperty("name")
    var name: String = name
    @JsonProperty("host")
    var host: String = host
}

@JsonTypeName("FixedUserName")
class FixedUserName (
    value: LiteralUserName     
): Node() {
    @JsonProperty("value")
    var value: LiteralUserName = value
}

@JsonTypeName("Variable")
class Variable (
    isSystem: Boolean? = null,
    name: String,
    value: String? = null     
): Primitive() {
    @JsonProperty("isSystem")
    var isSystem: Boolean? = isSystem
    @JsonProperty("name")
    var name: String = name
    @JsonProperty("value")
    var value: String? = value
}

@JsonTypeName("CharSet")
class CharSet (
    name: String     
): Node() {
    @JsonProperty("name")
    var name: String = name
}

@JsonTypeName("XIDName")
class XIDName (
    gtrid: String,
    bqual: String? = null,
    formatId: Int? = null     
): Node() {
    @JsonProperty("gtrid")
    var gtrid: String = gtrid
    @JsonProperty("bqual")
    var bqual: String? = bqual
    @JsonProperty("formatId")
    var formatId: Int? = formatId
}

@JsonTypeName("AuthPlugin")
class AuthPlugin (
    id: Identifier? = null,
    name: String? = null     
): Node() {
    @JsonProperty("id")
    var id: Identifier? = id
    @JsonProperty("name")
    var name: String? = name
}

@JsonTypeName("DbName")
class DbName (
    db: Identifier     
): Node() {
    @JsonProperty("db")
    var db: Identifier = db
}

@JsonTypeName("SchemaName")
class SchemaName (
    db: Identifier? = null,
    schema: Identifier     
): Node() {
    @JsonProperty("db")
    var db: Identifier? = db
    @JsonProperty("schema")
    var schema: Identifier = schema
}

@JsonTypeName("IndexName")
class IndexName (
    name: Identifier     
): Node() {
    @JsonProperty("name")
    var name: Identifier = name
}

@JsonTypeName("ViewName")
class ViewName (
    db: Identifier? = null,
    schema: Identifier? = null,
    view: Identifier     
): FullName() {
    @JsonProperty("db")
    var db: Identifier? = db
    @JsonProperty("schema")
    var schema: Identifier? = schema
    @JsonProperty("view")
    var view: Identifier = view
}

@JsonTypeName("TriggerName")
class TriggerName (
    db: Identifier? = null,
    schema: Identifier? = null,
    trigger: Identifier     
): FullName() {
    @JsonProperty("db")
    var db: Identifier? = db
    @JsonProperty("schema")
    var schema: Identifier? = schema
    @JsonProperty("trigger")
    var trigger: Identifier = trigger
}

@JsonTypeName("EventName")
class EventName (
    db: Identifier? = null,
    schema: Identifier? = null,
    event: Identifier     
): FullName() {
    @JsonProperty("db")
    var db: Identifier? = db
    @JsonProperty("schema")
    var schema: Identifier? = schema
    @JsonProperty("event")
    var event: Identifier = event
}

@JsonTypeName("ProcedureName")
class ProcedureName (
    db: Identifier? = null,
    schema: Identifier? = null,
    routine: Identifier     
): FullName() {
    @JsonProperty("db")
    var db: Identifier? = db
    @JsonProperty("schema")
    var schema: Identifier? = schema
    @JsonProperty("routine")
    var routine: Identifier = routine
}

@JsonTypeName("UDFunctionName")
class UDFunctionName (
    db: Identifier? = null,
    schema: Identifier? = null,
    routine: Identifier     
): FullName() {
    @JsonProperty("db")
    var db: Identifier? = db
    @JsonProperty("schema")
    var schema: Identifier? = schema
    @JsonProperty("routine")
    var routine: Identifier = routine
}

@JsonTypeName("TablespaceName")
class TablespaceName (
    name: Identifier     
): Node() {
    @JsonProperty("name")
    var name: Identifier = name
}

@JsonTypeName("LogFileGroupName")
class LogFileGroupName (
    name: Identifier     
): Node() {
    @JsonProperty("name")
    var name: Identifier = name
}

@JsonTypeName("ServerName")
class ServerName (
    name: Identifier     
): Node() {
    @JsonProperty("name")
    var name: Identifier = name
}

@JsonTypeName("Range")
class Range (
    start: Expression,
    end: Expression,
    separator: String     
): Node() {
    @JsonProperty("start")
    var start: Expression = start
    @JsonProperty("end")
    var end: Expression = end
    @JsonProperty("separator")
    var separator: String = separator
}

@JsonTypeName("Star")
class Star: Node() {

}

@JsonTypeName("Identifier")
class Identifier (
    name: String     
): Primitive() {
    @JsonProperty("name")
    var name: String = name
}

@JsonTypeName("Literal")
open class Literal: Primitive() {

}

@JsonTypeName("StringLiteral")
class StringLiteral (
    value: String     
): Literal() {
    @JsonProperty("value")
    var value: String = value
}

@JsonTypeName("RealLiteral")
class RealLiteral (
    value: String     
): Literal() {
    @JsonProperty("value")
    var value: String = value
}

@JsonTypeName("HexadecimalLiteral")
class HexadecimalLiteral (
    value: String     
): Literal() {
    @JsonProperty("value")
    var value: String = value
}

@JsonTypeName("BitStringLiteral")
class BitStringLiteral (
    value: String     
): Literal() {
    @JsonProperty("value")
    var value: String = value
}

@JsonTypeName("NullLiteral")
class NullLiteral (
    value: String     
): Literal() {
    @JsonProperty("value")
    var value: String = value
}

@JsonTypeName("NotNullLiteral")
class NotNullLiteral (
    value: String     
): Literal() {
    @JsonProperty("value")
    var value: String = value
}

@JsonTypeName("BooleanLiteral")
class BooleanLiteral (
    value: Boolean     
): Literal() {
    @JsonProperty("value")
    var value: Boolean = value
}

@JsonTypeName("NumberLiteral")
class NumberLiteral (
    value: String     
): Literal() {
    @JsonProperty("value")
    var value: String = value
}

@JsonTypeName("DataTypeClause")
open class DataTypeClause: Node() {

}

@JsonTypeName("SimpleDataTypeClause")
class SimpleDataTypeClause (
    typeName: DataType     
): DataTypeClause() {
    @JsonProperty("typeName")
    var typeName: DataType = typeName
}

@JsonTypeName("SpatialDataTypeClause")
class SpatialDataTypeClause (
    typeName: SpatialDataType     
): DataTypeClause() {
    @JsonProperty("typeName")
    var typeName: SpatialDataType = typeName
}

@JsonTypeName("DimensionDataTypeClause")
class DimensionDataTypeClause (
    typeName: DataType,
    length: Int? = null,
    secondLength: Int? = null,
    isUnsigned: Boolean? = null,
    isZerofill: Boolean? = null     
): DataTypeClause() {
    @JsonProperty("typeName")
    var typeName: DataType = typeName
    @JsonProperty("length")
    var length: Int? = length
    @JsonProperty("secondLength")
    var secondLength: Int? = secondLength
    @JsonProperty("isUnsigned")
    var isUnsigned: Boolean? = isUnsigned
    @JsonProperty("isZerofill")
    var isZerofill: Boolean? = isZerofill
}

@JsonTypeName("CharDataTypeClause")
class CharDataTypeClause (
    typeName: DataType,
    length: Int? = null,
    isBinary: Boolean,
    charSetName: CharSet? = null,
    collationName: String? = null     
): DataTypeClause() {
    @JsonProperty("typeName")
    var typeName: DataType = typeName
    @JsonProperty("length")
    var length: Int? = length
    @JsonProperty("isBinary")
    var isBinary: Boolean = isBinary
    @JsonProperty("charSetName")
    var charSetName: CharSet? = charSetName
    @JsonProperty("collationName")
    var collationName: String? = collationName
}

@JsonTypeName("CollectionCharDataTypeClause")
class CollectionCharDataTypeClause (
    typeName: DataType,
    isBinary: Boolean,
    charSetName: CharSet? = null,
    collationName: String? = null,
    values: MutableList<Literal>     
): DataTypeClause() {
    @JsonProperty("typeName")
    var typeName: DataType = typeName
    @JsonProperty("isBinary")
    var isBinary: Boolean = isBinary
    @JsonProperty("charSetName")
    var charSetName: CharSet? = charSetName
    @JsonProperty("collationName")
    var collationName: String? = collationName
    @JsonProperty("values")
    var values: MutableList<Literal> = values
}

@JsonTypeName("ConvertedDataType")
class ConvertedDataType (
    dataType: ConvertedDataTypeValue,
    firstDim: Int? = null,
    secondDim: Int? = null,
    charSet: CharSet? = null     
): Node() {
    @JsonProperty("dataType")
    var dataType: ConvertedDataTypeValue = dataType
    @JsonProperty("firstDim")
    var firstDim: Int? = firstDim
    @JsonProperty("secondDim")
    var secondDim: Int? = secondDim
    @JsonProperty("charSet")
    var charSet: CharSet? = charSet
}

@JsonTypeName("FunctionCall")
open class FunctionCall: Primitive() {

}

@JsonTypeName("UDFunctionCall")
class UDFunctionCall (
    name: UDFunctionName,
    arguments: MutableList<Expression>? = null     
): FunctionCall() {
    @JsonProperty("name")
    var name: UDFunctionName = name
    @JsonProperty("arguments")
    var arguments: MutableList<Expression>? = arguments
}

@JsonTypeName("SimpleFunctionCall")
class SimpleFunctionCall (
    name: String,
    arguments: MutableList<Expression>,
    over: OverClause? = null     
): FunctionCall() {
    @JsonProperty("name")
    var name: String = name
    @JsonProperty("arguments")
    var arguments: MutableList<Expression> = arguments
    @JsonProperty("over")
    var over: OverClause? = over
}

@JsonTypeName("AggregateFunctionCall")
class AggregateFunctionCall (
    name: String,
    aggregator: RowAggregator? = null,
    arguments: MutableList<Expression>,
    orders: MutableList<SortItem>,
    separator: String? = null,
    over: OverClause? = null     
): FunctionCall() {
    @JsonProperty("name")
    var name: String = name
    @JsonProperty("aggregator")
    var aggregator: RowAggregator? = aggregator
    @JsonProperty("arguments")
    var arguments: MutableList<Expression> = arguments
    @JsonProperty("orders")
    var orders: MutableList<SortItem> = orders
    @JsonProperty("separator")
    var separator: String? = separator
    @JsonProperty("over")
    var over: OverClause? = over
}

@JsonTypeName("CaseFunctionCall")
class CaseFunctionCall (
    expression: Expression? = null,
    cases: MutableList<CaseClause>,
    elseCase: Expression? = null     
): FunctionCall() {
    @JsonProperty("expression")
    var expression: Expression? = expression
    @JsonProperty("cases")
    var cases: MutableList<CaseClause> = cases
    @JsonProperty("elseCase")
    var elseCase: Expression? = elseCase
}

@JsonTypeName("CaseClause")
class CaseClause (
    whenClause: Expression,
    thenClause: Expression     
): Node() {
    @JsonProperty("whenClause")
    var whenClause: Expression = whenClause
    @JsonProperty("thenClause")
    var thenClause: Expression = thenClause
}

@JsonTypeName("ShortFormFunctionCall")
class ShortFormFunctionCall (
    name: String     
): FunctionCall() {
    @JsonProperty("name")
    var name: String = name
}

@JsonTypeName("ComplexFunctionCall")
class ComplexFunctionCall (
    name: String,
    arguments: MutableList<ComplexArgument>     
): FunctionCall() {
    @JsonProperty("name")
    var name: String = name
    @JsonProperty("arguments")
    var arguments: MutableList<ComplexArgument> = arguments
}

@JsonTypeName("PasswordFunctionCall")
class PasswordFunctionCall (
    nameFormat: SyntaxFormat,
    argument: Expression     
): FunctionCall() {
    @JsonProperty("nameFormat")
    var nameFormat: SyntaxFormat = nameFormat
    @JsonProperty("argument")
    var argument: Expression = argument
}

@JsonTypeName("OverClause")
class OverClause (
    overPartitions: MutableList<Expression>,
    orders: MutableList<SortItem>,
    ranges: MutableList<ExpressionArgument>     
): Node() {
    @JsonProperty("overPartitions")
    var overPartitions: MutableList<Expression> = overPartitions
    @JsonProperty("orders")
    var orders: MutableList<SortItem> = orders
    @JsonProperty("ranges")
    var ranges: MutableList<ExpressionArgument> = ranges
}

@JsonTypeName("ComplexArgument")
open class ComplexArgument: Node() {

}

@JsonTypeName("ExpressionArgument")
class ExpressionArgument (
    keyword: String? = null,
    keywordPosition: KeywordPosition? = null,
    value: Expression,
    separator: String? = null     
): ComplexArgument() {
    @JsonProperty("keyword")
    var keyword: String? = keyword
    @JsonProperty("keywordPosition")
    var keywordPosition: KeywordPosition? = keywordPosition
    @JsonProperty("value")
    var value: Expression = value
    @JsonProperty("separator")
    var separator: String? = separator
}

@JsonTypeName("KeywordArgument")
class KeywordArgument (
    keyword: String,
    separator: String? = null     
): ComplexArgument() {
    @JsonProperty("keyword")
    var keyword: String = keyword
    @JsonProperty("separator")
    var separator: String? = separator
}

@JsonTypeName("TypedArgument")
class TypedArgument (
    keyword: String? = null,
    keywordPosition: KeywordPosition? = null,
    value: ConvertedDataType,
    separator: String? = null     
): ComplexArgument() {
    @JsonProperty("keyword")
    var keyword: String? = keyword
    @JsonProperty("keywordPosition")
    var keywordPosition: KeywordPosition? = keywordPosition
    @JsonProperty("value")
    var value: ConvertedDataType = value
    @JsonProperty("separator")
    var separator: String? = separator
}

@JsonTypeName("CharsetArgument")
class CharsetArgument (
    keyword: String? = null,
    keywordPosition: KeywordPosition? = null,
    value: CharSet,
    separator: String? = null     
): ComplexArgument() {
    @JsonProperty("keyword")
    var keyword: String? = keyword
    @JsonProperty("keywordPosition")
    var keywordPosition: KeywordPosition? = keywordPosition
    @JsonProperty("value")
    var value: CharSet = value
    @JsonProperty("separator")
    var separator: String? = separator
}

@JsonTypeName("NestedArgument")
class NestedArgument (
    keyword: String? = null,
    keywordPosition: KeywordPosition? = null,
    values: MutableList<ComplexArgument>     
): ComplexArgument() {
    @JsonProperty("keyword")
    var keyword: String? = keyword
    @JsonProperty("keywordPosition")
    var keywordPosition: KeywordPosition? = keywordPosition
    @JsonProperty("values")
    var values: MutableList<ComplexArgument> = values
}

@JsonTypeName("Expression")
open class Expression: Node() {

}

@JsonTypeName("Predicate")
open class Predicate: Expression() {

}

@JsonTypeName("Primitive")
open class Primitive: Predicate() {

}

@JsonTypeName("LogicalExpression")
class LogicalExpression (
    isUnary: Boolean,
    operator: LogicalOperator,
    left: Expression,
    right: Expression? = null     
): Expression() {
    @JsonProperty("isUnary")
    var isUnary: Boolean = isUnary
    @JsonProperty("operator")
    var operator: LogicalOperator = operator
    @JsonProperty("left")
    var left: Expression = left
    @JsonProperty("right")
    var right: Expression? = right
}

@JsonTypeName("IsExpression")
class IsExpression (
    notArgument: Boolean,
    value: Predicate,
    match: LogicalMatch     
): Expression() {
    @JsonProperty("notArgument")
    var notArgument: Boolean = notArgument
    @JsonProperty("value")
    var value: Predicate = value
    @JsonProperty("match")
    var match: LogicalMatch = match
}

@JsonTypeName("IsNullPredicate")
class IsNullPredicate (
    notArgument: Boolean,
    value: Predicate     
): Predicate() {
    @JsonProperty("notArgument")
    var notArgument: Boolean = notArgument
    @JsonProperty("value")
    var value: Predicate = value
}

@JsonTypeName("ComparisonPredicate")
class ComparisonPredicate (
    operator: ComparisonOperator,
    left: Predicate,
    right: Predicate     
): Predicate() {
    @JsonProperty("operator")
    var operator: ComparisonOperator = operator
    @JsonProperty("left")
    var left: Predicate = left
    @JsonProperty("right")
    var right: Predicate = right
}

@JsonTypeName("ComparisonSetPredicate")
class ComparisonSetPredicate (
    operator: ComparisonOperator,
    quantifier: QuantifierType,
    value: Predicate,
    subquery: SubqueryExpression     
): Predicate() {
    @JsonProperty("operator")
    var operator: ComparisonOperator = operator
    @JsonProperty("quantifier")
    var quantifier: QuantifierType = quantifier
    @JsonProperty("value")
    var value: Predicate = value
    @JsonProperty("subquery")
    var subquery: SubqueryExpression = subquery
}

@JsonTypeName("InPredicate")
class InPredicate (
    isSubquery: Boolean,
    notArgument: Boolean,
    subquery: SubqueryExpression? = null,
    comparableValue: Predicate,
    comparedValues: MutableList<Expression>     
): Predicate() {
    @JsonProperty("isSubquery")
    var isSubquery: Boolean = isSubquery
    @JsonProperty("notArgument")
    var notArgument: Boolean = notArgument
    @JsonProperty("subquery")
    var subquery: SubqueryExpression? = subquery
    @JsonProperty("comparableValue")
    var comparableValue: Predicate = comparableValue
    @JsonProperty("comparedValues")
    var comparedValues: MutableList<Expression> = comparedValues
}

@JsonTypeName("BetweenPredicate")
class BetweenPredicate (
    notArgument: Boolean,
    value: Predicate,
    left: Predicate,
    right: Predicate     
): Predicate() {
    @JsonProperty("notArgument")
    var notArgument: Boolean = notArgument
    @JsonProperty("value")
    var value: Predicate = value
    @JsonProperty("left")
    var left: Predicate = left
    @JsonProperty("right")
    var right: Predicate = right
}

@JsonTypeName("LikePredicate")
class LikePredicate (
    notArgument: Boolean,
    operator: TypeLike,
    value: Predicate,
    pattern: Predicate,
    escapeString: String? = null     
): Predicate() {
    @JsonProperty("notArgument")
    var notArgument: Boolean = notArgument
    @JsonProperty("operator")
    var operator: TypeLike = operator
    @JsonProperty("value")
    var value: Predicate = value
    @JsonProperty("pattern")
    var pattern: Predicate = pattern
    @JsonProperty("escapeString")
    var escapeString: String? = escapeString
}

@JsonTypeName("UnaryExpression")
class UnaryExpression (
    operator: UnaryOperator,
    value: Primitive     
): Primitive() {
    @JsonProperty("operator")
    var operator: UnaryOperator = operator
    @JsonProperty("value")
    var value: Primitive = value
}

@JsonTypeName("BinaryExpression")
class BinaryExpression (
    operator: BinaryOperator,
    left: Primitive,
    right: Primitive     
): Primitive() {
    @JsonProperty("operator")
    var operator: BinaryOperator = operator
    @JsonProperty("left")
    var left: Primitive = left
    @JsonProperty("right")
    var right: Primitive = right
}

@JsonTypeName("ParenthesisExpression")
class ParenthesisExpression (
    value: Expression     
): Primitive() {
    @JsonProperty("value")
    var value: Expression = value
}

@JsonTypeName("ExistsExpression")
class ExistsExpression (
    subquery: SubqueryExpression     
): Primitive() {
    @JsonProperty("subquery")
    var subquery: SubqueryExpression = subquery
}

@JsonTypeName("SubqueryExpression")
class SubqueryExpression (
    subquery: CommonSelectStatement     
): Primitive() {
    @JsonProperty("subquery")
    var subquery: CommonSelectStatement = subquery
}

@JsonTypeName("IntervalExpression")
class IntervalExpression (
    intervalType: IntervalType,
    value: Expression     
): Primitive() {
    @JsonProperty("intervalType")
    var intervalType: IntervalType = intervalType
    @JsonProperty("value")
    var value: Expression = value
}

@JsonTypeName("KeywordPrimitive")
class KeywordPrimitive (
    keyword: KeywordLiteral     
): Primitive() {
    @JsonProperty("keyword")
    var keyword: KeywordLiteral = keyword
}

@JsonTypeName("RowPrimitive")
class RowPrimitive (
    isTuple: Boolean,
    values: MutableList<Expression>     
): Primitive() {
    @JsonProperty("isTuple")
    var isTuple: Boolean = isTuple
    @JsonProperty("values")
    var values: MutableList<Expression> = values
}

@JsonTypeName("StringPrimitive")
class StringPrimitive (
    transformationType: StringTransformType,
    value: Primitive,
    collationName: String? = null     
): Primitive() {
    @JsonProperty("transformationType")
    var transformationType: StringTransformType = transformationType
    @JsonProperty("value")
    var value: Primitive = value
    @JsonProperty("collationName")
    var collationName: String? = collationName
}

@JsonTypeName("CommonSimpleOption")
open class CommonSimpleOption: Node() {

}

@JsonTypeName("StringSimpleOption")
class StringSimpleOption (
    name: String,
    value: String,
    format: SyntaxFormat? = null     
): CommonSimpleOption() {
    @JsonProperty("name")
    var name: String = name
    @JsonProperty("value")
    var value: String = value
    @JsonProperty("format")
    var format: SyntaxFormat? = format
}

@JsonTypeName("ListStringSimpleOption")
class ListStringSimpleOption (
    name: String,
    value: MutableList<String>,
    format: SyntaxFormat? = null     
): CommonSimpleOption() {
    @JsonProperty("name")
    var name: String = name
    @JsonProperty("value")
    var value: MutableList<String> = value
    @JsonProperty("format")
    var format: SyntaxFormat? = format
}

@JsonTypeName("NumberSimpleOption")
class NumberSimpleOption (
    name: String,
    value: Int,
    format: SyntaxFormat? = null     
): CommonSimpleOption() {
    @JsonProperty("name")
    var name: String = name
    @JsonProperty("value")
    var value: Int = value
    @JsonProperty("format")
    var format: SyntaxFormat? = format
}

@JsonTypeName("BooleanSimpleOption")
class BooleanSimpleOption (
    name: String,
    value: Boolean,
    format: SyntaxFormat? = null     
): CommonSimpleOption() {
    @JsonProperty("name")
    var name: String = name
    @JsonProperty("value")
    var value: Boolean = value
    @JsonProperty("format")
    var format: SyntaxFormat? = format
}

@JsonTypeName("NodeSimpleOption")
class NodeSimpleOption (
    name: String,
    value: Node,
    format: SyntaxFormat? = null     
): CommonSimpleOption() {
    @JsonProperty("name")
    var name: String = name
    @JsonProperty("value")
    var value: Node = value
    @JsonProperty("format")
    var format: SyntaxFormat? = format
}

@JsonTypeName("ListSimpleOption")
class ListSimpleOption (
    name: String,
    value: MutableList<Node>,
    format: SyntaxFormat? = null     
): CommonSimpleOption() {
    @JsonProperty("name")
    var name: String = name
    @JsonProperty("value")
    var value: MutableList<Node> = value
    @JsonProperty("format")
    var format: SyntaxFormat? = format
}

