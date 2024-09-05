// Generated from //wsl.localhost/Ubuntu/home/linky/Universidad/LenguajesDeProgramacion/Parcial1/Punto5/CalcTrig.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CalcTrigParser}.
 */
public interface CalcTrigListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CalcTrigParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(CalcTrigParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link CalcTrigParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(CalcTrigParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by the {@code printExpr}
	 * labeled alternative in {@link CalcTrigParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterPrintExpr(CalcTrigParser.PrintExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code printExpr}
	 * labeled alternative in {@link CalcTrigParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitPrintExpr(CalcTrigParser.PrintExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code SinFunction}
	 * labeled alternative in {@link CalcTrigParser#function}.
	 * @param ctx the parse tree
	 */
	void enterSinFunction(CalcTrigParser.SinFunctionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code SinFunction}
	 * labeled alternative in {@link CalcTrigParser#function}.
	 * @param ctx the parse tree
	 */
	void exitSinFunction(CalcTrigParser.SinFunctionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code CosFunction}
	 * labeled alternative in {@link CalcTrigParser#function}.
	 * @param ctx the parse tree
	 */
	void enterCosFunction(CalcTrigParser.CosFunctionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code CosFunction}
	 * labeled alternative in {@link CalcTrigParser#function}.
	 * @param ctx the parse tree
	 */
	void exitCosFunction(CalcTrigParser.CosFunctionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code TanFunction}
	 * labeled alternative in {@link CalcTrigParser#function}.
	 * @param ctx the parse tree
	 */
	void enterTanFunction(CalcTrigParser.TanFunctionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code TanFunction}
	 * labeled alternative in {@link CalcTrigParser#function}.
	 * @param ctx the parse tree
	 */
	void exitTanFunction(CalcTrigParser.TanFunctionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code int}
	 * labeled alternative in {@link CalcTrigParser#num}.
	 * @param ctx the parse tree
	 */
	void enterInt(CalcTrigParser.IntContext ctx);
	/**
	 * Exit a parse tree produced by the {@code int}
	 * labeled alternative in {@link CalcTrigParser#num}.
	 * @param ctx the parse tree
	 */
	void exitInt(CalcTrigParser.IntContext ctx);
}