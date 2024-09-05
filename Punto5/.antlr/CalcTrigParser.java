// Generated from //wsl.localhost/Ubuntu/home/linky/Universidad/LenguajesDeProgramacion/Parcial1/Punto5/CalcTrig.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class CalcTrigParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, SIN=3, COS=4, TAN=5, INT=6, WS=7;
	public static final int
		RULE_prog = 0, RULE_stat = 1, RULE_function = 2, RULE_num = 3;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "stat", "function", "num"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'sin'", "'cos'", "'tan'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "SIN", "COS", "TAN", "INT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "CalcTrig.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CalcTrigParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(9); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(8);
				stat();
				}
				}
				setState(11); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 56L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatContext extends ParserRuleContext {
		public StatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stat; }
	 
		public StatContext() { }
		public void copyFrom(StatContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PrintExprContext extends StatContext {
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public PrintExprContext(StatContext ctx) { copyFrom(ctx); }
	}

	public final StatContext stat() throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_stat);
		try {
			_localctx = new PrintExprContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(13);
			function();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionContext extends ParserRuleContext {
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	 
		public FunctionContext() { }
		public void copyFrom(FunctionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CosFunctionContext extends FunctionContext {
		public TerminalNode COS() { return getToken(CalcTrigParser.COS, 0); }
		public NumContext num() {
			return getRuleContext(NumContext.class,0);
		}
		public CosFunctionContext(FunctionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SinFunctionContext extends FunctionContext {
		public TerminalNode SIN() { return getToken(CalcTrigParser.SIN, 0); }
		public NumContext num() {
			return getRuleContext(NumContext.class,0);
		}
		public SinFunctionContext(FunctionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class TanFunctionContext extends FunctionContext {
		public TerminalNode TAN() { return getToken(CalcTrigParser.TAN, 0); }
		public NumContext num() {
			return getRuleContext(NumContext.class,0);
		}
		public TanFunctionContext(FunctionContext ctx) { copyFrom(ctx); }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_function);
		try {
			setState(30);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SIN:
				_localctx = new SinFunctionContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(15);
				match(SIN);
				setState(16);
				match(T__0);
				setState(17);
				num();
				setState(18);
				match(T__1);
				}
				break;
			case COS:
				_localctx = new CosFunctionContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(20);
				match(COS);
				setState(21);
				match(T__0);
				setState(22);
				num();
				setState(23);
				match(T__1);
				}
				break;
			case TAN:
				_localctx = new TanFunctionContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(25);
				match(TAN);
				setState(26);
				match(T__0);
				setState(27);
				num();
				setState(28);
				match(T__1);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumContext extends ParserRuleContext {
		public NumContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_num; }
	 
		public NumContext() { }
		public void copyFrom(NumContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntContext extends NumContext {
		public TerminalNode INT() { return getToken(CalcTrigParser.INT, 0); }
		public IntContext(NumContext ctx) { copyFrom(ctx); }
	}

	public final NumContext num() throws RecognitionException {
		NumContext _localctx = new NumContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_num);
		try {
			_localctx = new IntContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			match(INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0007#\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0001\u0000\u0004\u0000\n\b"+
		"\u0000\u000b\u0000\f\u0000\u000b\u0001\u0001\u0001\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0003\u0002\u001f\b\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0000\u0000\u0004\u0000\u0002\u0004\u0006\u0000\u0000!\u0000\t"+
		"\u0001\u0000\u0000\u0000\u0002\r\u0001\u0000\u0000\u0000\u0004\u001e\u0001"+
		"\u0000\u0000\u0000\u0006 \u0001\u0000\u0000\u0000\b\n\u0003\u0002\u0001"+
		"\u0000\t\b\u0001\u0000\u0000\u0000\n\u000b\u0001\u0000\u0000\u0000\u000b"+
		"\t\u0001\u0000\u0000\u0000\u000b\f\u0001\u0000\u0000\u0000\f\u0001\u0001"+
		"\u0000\u0000\u0000\r\u000e\u0003\u0004\u0002\u0000\u000e\u0003\u0001\u0000"+
		"\u0000\u0000\u000f\u0010\u0005\u0003\u0000\u0000\u0010\u0011\u0005\u0001"+
		"\u0000\u0000\u0011\u0012\u0003\u0006\u0003\u0000\u0012\u0013\u0005\u0002"+
		"\u0000\u0000\u0013\u001f\u0001\u0000\u0000\u0000\u0014\u0015\u0005\u0004"+
		"\u0000\u0000\u0015\u0016\u0005\u0001\u0000\u0000\u0016\u0017\u0003\u0006"+
		"\u0003\u0000\u0017\u0018\u0005\u0002\u0000\u0000\u0018\u001f\u0001\u0000"+
		"\u0000\u0000\u0019\u001a\u0005\u0005\u0000\u0000\u001a\u001b\u0005\u0001"+
		"\u0000\u0000\u001b\u001c\u0003\u0006\u0003\u0000\u001c\u001d\u0005\u0002"+
		"\u0000\u0000\u001d\u001f\u0001\u0000\u0000\u0000\u001e\u000f\u0001\u0000"+
		"\u0000\u0000\u001e\u0014\u0001\u0000\u0000\u0000\u001e\u0019\u0001\u0000"+
		"\u0000\u0000\u001f\u0005\u0001\u0000\u0000\u0000 !\u0005\u0006\u0000\u0000"+
		"!\u0007\u0001\u0000\u0000\u0000\u0002\u000b\u001e";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}