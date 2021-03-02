
"""
Note that this file is autogenerated by `integration_test_factory.py`
and changes are likely to be overwritten.
"""

import unittest
from .test_utils import runner, assert_frames_close

rtol = .05


class TestIntegrationExamples(unittest.TestCase):

    def test_abs(self):
        output, canon = runner('test-models/tests/abs/test_abs.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_active_initial(self):
        output, canon = runner('test-models/tests/active_initial/test_active_initial.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_arguments(self):
        output, canon = runner('test-models/tests/arguments/test_arguments.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_builtin_max(self):
        output, canon = runner('test-models/tests/builtin_max/builtin_max.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_builtin_min(self):
        output, canon = runner('test-models/tests/builtin_min/builtin_min.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_chained_initialization(self):
        output, canon = runner('test-models/tests/chained_initialization/test_chained_initialization.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_constant_expressions(self):
        output, canon = runner('test-models/tests/constant_expressions/test_constant_expressions.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    @unittest.skip('to be fixed #225')
    def test_delay_numeric_error(self):
        # issue https://github.com/JamesPHoughton/pysd/issues/225
        output, canon = runner('test-models/tests/delay_numeric_error/test_delay_numeric_error.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_delay_parentheses(self):
        output, canon = runner('test-models/tests/delay_parentheses/test_delay_parentheses.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    @unittest.skip('to be fixed #147')
    def test_delay_pipeline(self):
        # issue https://github.com/JamesPHoughton/pysd/issues/147
        output, canon = runner('test-models/tests/delay_pipeline/test_pipeline_delays.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    @unittest.skip('to be fixed #147')
    def test_delays(self):
        # issue https://github.com/JamesPHoughton/pysd/issues/147
        output, canon = runner('test-models/tests/delays/test_delays.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_euler_step_vs_saveper(self):
        output, canon = runner('test-models/tests/euler_step_vs_saveper/test_euler_step_vs_saveper.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_exp(self):
        output, canon = runner('test-models/tests/exp/test_exp.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_exponentiation(self):
        output, canon = runner('test-models/tests/exponentiation/exponentiation.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_function_capitalization(self):
        output, canon = runner('test-models/tests/function_capitalization/test_function_capitalization.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_game(self):
        output, canon = runner('test-models/tests/game/test_game.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_get_data_args_3d_xls(self):
        """
        Test for usage of GET DIRECT/XLS DATA with arguments from a Excel file
        All the possible combinations of lentgh-wise and different dimensions
        are tested in unit_test_external.py, this test want to test only the
        good working of the builder
        """
        output, canon = runner(
          'test-models/tests/get_data_args_3d_xls/'
          + 'test_get_data_args_3d_xls.mdl'
        )
        assert_frames_close(output, canon, rtol=rtol)

    def test_get_lookups_data_3d_xls(self):
        """
        Test for usage of GET DIRECT/XLS LOOKUPS/DATA from a Excel file
        All the possible combinations of lentgh-wise and different dimensions
        are tested in unit_test_external.py, this test want to test only the
        good working of the builder
        """
        output, canon = runner(
          'test-models/tests/get_lookups_data_3d_xls/'
          + 'test_get_lookups_data_3d_xls.mdl'
        )
        assert_frames_close(output, canon, rtol=rtol)

    def test_get_lookups_subscripted_args(self):
        import warnings

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            output, canon = runner(
              'test-models/tests/get_lookups_subscripted_args/'
              + 'test_get_lookups_subscripted_args.mdl'
            )
        assert_frames_close(output, canon, rtol=rtol)

    def test_get_lookups_subset(self):
        output, canon = runner(
          'test-models/tests/get_lookups_subset/'
          + 'test_get_lookups_subset.mdl'
        )
        assert_frames_close(output, canon, rtol=rtol)

    def test_get_with_missing_values_xlsx(self):
        import warnings

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            output, canon = runner(
                'test-models/tests/get_with_missing_values_xlsx/'
                + 'test_get_with_missing_values_xlsx.mdl'
            )

        assert_frames_close(output, canon, rtol=rtol)

    def test_get_mixed_definitions(self):
        output, canon = runner(
          'test-models/tests/get_mixed_definitions/'
          + 'test_get_mixed_definitions.mdl'
        )
        assert_frames_close(output, canon, rtol=rtol)

    def test_get_subscript_3d_arrays_xls(self):
        """
        Test for usage of GET DIRECT/XLS SUBSCRIPTS/CONSTANTS from a Excel file
        All the possible combinations of lentgh-wise and different dimensions
        are tested in unit_test_external.py, this test want to test only the
        good working of the builder
        """
        output, canon = runner(
          'test-models/tests/get_subscript_3d_arrays_xls/'
          + 'test_get_subscript_3d_arrays_xls.mdl'
        )
        assert_frames_close(output, canon, rtol=rtol)

    def test_get_xls_cellrange(self):
        output, canon = runner(
          'test-models/tests/get_xls_cellrange/'
          + 'test_get_xls_cellrange.mdl'
        )
        assert_frames_close(output, canon, rtol=rtol)

    def test_if_stmt(self):
        output, canon = runner('test-models/tests/if_stmt/if_stmt.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_initial_function(self):
        output, canon = runner('test-models/tests/initial_function/test_initial.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_input_functions(self):
        output, canon = runner('test-models/tests/input_functions/test_inputs.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_limits(self):
        output, canon = runner('test-models/tests/limits/test_limits.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_line_breaks(self):
        output, canon = runner('test-models/tests/line_breaks/test_line_breaks.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_line_continuation(self):
        output, canon = runner('test-models/tests/line_continuation/test_line_continuation.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_ln(self):
        output, canon = runner('test-models/tests/ln/test_ln.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_log(self):
        output, canon = runner('test-models/tests/log/test_log.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_logicals(self):
        output, canon = runner('test-models/tests/logicals/test_logicals.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_lookups(self):
        output, canon = runner('test-models/tests/lookups/test_lookups.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_lookups_without_range(self):
        output, canon = runner('test-models/tests/lookups_without_range/test_lookups_without_range.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_lookups_funcnames(self):
        output, canon = runner('test-models/tests/lookups_funcnames/test_lookups_funcnames.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_lookups_inline(self):
        output, canon = runner('test-models/tests/lookups_inline/test_lookups_inline.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_lookups_inline_bounded(self):
        output, canon = runner('test-models/tests/lookups_inline_bounded/test_lookups_inline_bounded.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_lookups_with_expr(self):
        output, canon = runner('test-models/tests/lookups_with_expr/test_lookups_with_expr.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_macro_cross_reference(self):
        output, canon = runner('test-models/tests/macro_cross_reference/test_macro_cross_reference.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_macro_expression(self):
        output, canon = runner('test-models/tests/macro_expression/test_macro_expression.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_macro_multi_expression(self):
        output, canon = runner('test-models/tests/macro_multi_expression/test_macro_multi_expression.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_macro_multi_macros(self):
        output, canon = runner('test-models/tests/macro_multi_macros/test_macro_multi_macros.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    @unittest.skip('working')
    def test_macro_output(self):
        output, canon = runner('test-models/tests/macro_output/test_macro_output.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_macro_stock(self):
        output, canon = runner('test-models/tests/macro_stock/test_macro_stock.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    @unittest.skip('do we need this?')
    def test_macro_trailing_definition(self):
        output, canon = runner('test-models/tests/macro_trailing_definition/test_macro_trailing_definition.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_model_doc(self):
        output, canon = runner('test-models/tests/model_doc/model_doc.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_number_handling(self):
        output, canon = runner('test-models/tests/number_handling/test_number_handling.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_parentheses(self):
        output, canon = runner('test-models/tests/parentheses/test_parens.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    @unittest.skip('low priority')
    def test_reference_capitalization(self):
        """A properly formatted Vensim model should never create this failure"""
        output, canon = runner('test-models/tests/reference_capitalization/test_reference_capitalization.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    @unittest.skip('in branch')
    def test_rounding(self):
        output, canon = runner('test-models/tests/rounding/test_rounding.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    @unittest.skip('working on it #217')
    def test_sample_if_true(self):
        # issue https://github.com/JamesPHoughton/pysd/issues/217
        output, canon = runner('test-models/tests/sample_if_true/test_sample_if_true.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_smooth(self):
        output, canon = runner('test-models/tests/smooth/test_smooth.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_smooth_and_stock(self):
        output, canon = runner('test-models/tests/smooth_and_stock/test_smooth_and_stock.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_special_characters(self):
        output, canon = runner('test-models/tests/special_characters/test_special_variable_names.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_sqrt(self):
        output, canon = runner('test-models/tests/sqrt/test_sqrt.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subrange_merge(self):
        output, canon = runner('test-models/tests/subrange_merge/test_subrange_merge.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_multiples(self):
        output, canon = runner('test-models/tests/subscript_multiples/test_multiple_subscripts.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_1d_arrays(self):
        output, canon = runner('test-models/tests/subscript_1d_arrays/test_subscript_1d_arrays.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_2d_arrays(self):
        output, canon = runner('test-models/tests/subscript_2d_arrays/test_subscript_2d_arrays.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_3d_arrays(self):
        output, canon = runner('test-models/tests/subscript_3d_arrays/test_subscript_3d_arrays.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_3d_arrays_lengthwise(self):
        output, canon = runner('test-models/tests/subscript_3d_arrays_lengthwise/test_subscript_3d_arrays_lengthwise.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_3d_arrays_widthwise(self):
        output, canon = runner('test-models/tests/subscript_3d_arrays_widthwise/test_subscript_3d_arrays_widthwise.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_aggregation(self):
        output, canon = runner('test-models/tests/subscript_aggregation/test_subscript_aggregation.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_constant_call(self):
        output, canon = runner('test-models/tests/subscript_constant_call/test_subscript_constant_call.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_docs(self):
        output, canon = runner('test-models/tests/subscript_docs/subscript_docs.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_element_name(self):
        # issue https://github.com/JamesPHoughton/pysd/issues/216
        output, canon = runner('test-models/tests/subscript_element_name/test_subscript_element_name.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_individually_defined_1_of_2d_arrays(self):
        output, canon = runner('test-models/tests/subscript_individually_defined_1_of_2d_arrays/subscript_individually_defined_1_of_2d_arrays.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_individually_defined_1_of_2d_arrays_from_floats(self):
        output, canon = runner('test-models/tests/subscript_individually_defined_1_of_2d_arrays_from_floats/subscript_individually_defined_1_of_2d_arrays_from_floats.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_individually_defined_1d_arrays(self):
        output, canon = runner('test-models/tests/subscript_individually_defined_1d_arrays/subscript_individually_defined_1d_arrays.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_individually_defined_stocks(self):
        output, canon = runner('test-models/tests/subscript_individually_defined_stocks/test_subscript_individually_defined_stocks.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_mixed_assembly(self):
        output, canon = runner('test-models/tests/subscript_mixed_assembly/test_subscript_mixed_assembly.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_selection(self):
        output, canon = runner('test-models/tests/subscript_selection/subscript_selection.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_subranges(self):
        output, canon = runner('test-models/tests/subscript_subranges/test_subscript_subrange.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_subranges_equal(self):
        output, canon = runner('test-models/tests/subscript_subranges_equal/test_subscript_subrange_equal.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_switching(self):
        output, canon = runner('test-models/tests/subscript_switching/subscript_switching.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_transposition(self):
        output, canon = runner('test-models/tests/subscript_transposition/test_subscript_transposition.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_updimensioning(self):
        output, canon = runner('test-models/tests/subscript_updimensioning/test_subscript_updimensioning.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscripted_delays(self):
        output, canon = runner('test-models/tests/subscripted_delays/test_subscripted_delays.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscripted_flows(self):
        output, canon = runner('test-models/tests/subscripted_flows/test_subscripted_flows.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscripted_if_then_else(self):
        output, canon = runner('test-models/tests/subscripted_if_then_else/test_subscripted_if_then_else.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    @unittest.skip('working on it #226')
    def test_subscripted_smooth(self):
        # issue https://github.com/JamesPHoughton/pysd/issues/226
        output, canon = runner('test-models/tests/subscripted_smooth/test_subscripted_smooth.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    @unittest.skip('working on it #226')
    def test_subscripted_trend(self):
        # issue https://github.com/JamesPHoughton/pysd/issues/226
        output, canon = runner('test-models/tests/subscripted_trend/test_subscripted_trend.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscripted_xidz(self):
        output, canon = runner('test-models/tests/subscripted_xidz/test_subscripted_xidz.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subset_duplicated_coord(self):
        output, canon = runner('test-models/tests/subset_duplicated_coord/'
                               + 'test_subset_duplicated_coord.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_time(self):
        output, canon = runner('test-models/tests/time/test_time.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_trend(self):
        output, canon = runner('test-models/tests/trend/test_trend.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_trig(self):
        output, canon = runner('test-models/tests/trig/test_trig.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_variable_ranges(self):
        output, canon = runner('test-models/tests/variable_ranges/test_variable_ranges.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_unicode_characters(self):
        output, canon = runner('test-models/tests/unicode_characters/unicode_test_model.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_xidz_zidz(self):
        output, canon = runner('test-models/tests/xidz_zidz/xidz_zidz.mdl')
        assert_frames_close(output, canon, rtol=rtol)


