
predefined_scans_base = "https://stockcharts.com/def/servlet/SC.scan"
searches = {
    "bullish ma cross": "?s=TSAL[t.t_eq_s]![T.E_EQ_N]![T.E_NE_O]![as0,20,tv_gt_40000]![as0,50,tc_gt_as0,200,tc]![as1,50,tc_le_as1,200,tc]&report=predefall",
    "bullish macd cross": "?s=TSAL[t.t_eq_s]![T.E_EQ_N]![T.E_NE_O]![as0,20,tv_gt_40000]![ba0_lt_0]![ba0_ge_bb0]![ba1_lt_bb1]![ba2_lt_bb2]![ba3_lt_bb3]&report=predefall",
    "oversold improve rsi": "?s=TSAL[t.t_eq_s]![T.E_EQ_N]![T.E_NE_O]![as0,20,tv_gt_40000]![bs0_gt_30]![bs1_lt_29]![bs2_lt_28]![bs3_lt_27]&report=predefall",
    "parabolic sar": "?s=TSAL[t.t_eq_s]![T.E_EQ_N]![T.E_NE_O]![as0,20,tv_gt_40000]![ap1,0.02,0.2_gt_tc1]![ap0,0.02,0.2_lt_tc0]&report=predefall"

}
abovesearch = {
    0: "bullish ma cross",
    1: "bullish macd cross",
    2: "oversold improve rsi",
    3: "parabolic sar"
}
