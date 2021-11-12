
"""
Note that this file is autogenerated by `integration_test_factory.py`
and changes are likely to be overwritten.
"""
import os
import warnings
import unittest
from pysd.tools.benchmarking import runner, assert_frames_close

rtol = .05

_root = os.path.dirname(__file__)
test_models = os.path.join(_root, "test-models/tests")


class TestIntegrationExamples(unittest.TestCase):

    def test_abs(self):
        output, canon = runner(test_models + '/abs/test_abs.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_active_initial(self):
        output, canon = runner(test_models + '/active_initial/test_active_initial.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_arguments(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            output, canon = runner(test_models + '/arguments/test_arguments.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_builtin_max(self):
        output, canon = runner(test_models + '/builtin_max/builtin_max.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_builtin_min(self):
        output, canon = runner(test_models + '/builtin_min/builtin_min.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_chained_initialization(self):
        output, canon = runner(test_models + '/chained_initialization/test_chained_initialization.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_control_vars(self):
        output, canon = runner(test_models + '/control_vars/test_control_vars.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_constant_expressions(self):
        output, canon = runner(test_models + '/constant_expressions/test_constant_expressions.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_data_from_other_model(self):
        output, canon = runner(
            test_models + '/data_from_other_model/test_data_from_other_model.mdl',
            data_files=test_models + '/data_from_other_model/data.tab')
        assert_frames_close(output, canon, rtol=rtol)

    def test_delay_fixed(self):
        # issue https://github.com/JamesPHoughton/pysd/issues/147
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            output, canon = runner(test_models + '/delay_fixed/test_delay_fixed.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_delay_numeric_error(self):
        # issue https://github.com/JamesPHoughton/pysd/issues/225
        output, canon = runner(test_models + '/delay_numeric_error/test_delay_numeric_error.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_delay_parentheses(self):
        output, canon = runner(test_models + '/delay_parentheses/test_delay_parentheses.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_delay_pipeline(self):
        # issue https://github.com/JamesPHoughton/pysd/issues/147
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            output, canon = runner(test_models + '/delay_pipeline/test_pipeline_delays.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_delays(self):
        # issue https://github.com/JamesPHoughton/pysd/issues/147
        output, canon = runner(test_models + '/delays/test_delays.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_dynamic_final_time(self):
        # issue https://github.com/JamesPHoughton/pysd/issues/278
        output, canon = runner(test_models + '/dynamic_final_time/test_dynamic_final_time.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_euler_step_vs_saveper(self):
        output, canon = runner(test_models + '/euler_step_vs_saveper/test_euler_step_vs_saveper.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_exp(self):
        output, canon = runner(test_models + '/exp/test_exp.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_exponentiation(self):
        output, canon = runner(test_models + '/exponentiation/exponentiation.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_forecast(self):
        output, canon = runner(test_models + '/forecast/test_forecast.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_function_capitalization(self):
        output, canon = runner(test_models + '/function_capitalization/test_function_capitalization.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_game(self):
        output, canon = runner(test_models + '/game/test_game.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_get_constants_subrange(self):
        output, canon = runner(
          test_models + '/get_constants_subranges/'
          + 'test_get_constants_subranges.mdl'
        )
        assert_frames_close(output, canon, rtol=rtol)

    def test_get_data_args_3d_xls(self):
        """
        Test for usage of GET DIRECT/XLS DATA with arguments from a Excel file
        All the possible combinations of lentgh-wise and different dimensions
        are tested in unit_test_external.py, this test want to test only the
        good working of the builder
        """
        output, canon = runner(
          test_models + '/get_data_args_3d_xls/'
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
          test_models + '/get_lookups_data_3d_xls/'
          + 'test_get_lookups_data_3d_xls.mdl'
        )
        assert_frames_close(output, canon, rtol=rtol)

    def test_get_lookups_subscripted_args(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            output, canon = runner(
              test_models + '/get_lookups_subscripted_args/'
              + 'test_get_lookups_subscripted_args.mdl'
            )
        assert_frames_close(output, canon, rtol=rtol)

    def test_get_lookups_subset(self):
        output, canon = runner(
          test_models + '/get_lookups_subset/'
          + 'test_get_lookups_subset.mdl'
        )
        assert_frames_close(output, canon, rtol=rtol)

    def test_get_with_missing_values_xlsx(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            output, canon = runner(
                test_models + '/get_with_missing_values_xlsx/'
                + 'test_get_with_missing_values_xlsx.mdl'
            )

        assert_frames_close(output, canon, rtol=rtol)

    def test_get_mixed_definitions(self):
        output, canon = runner(
          test_models + '/get_mixed_definitions/'
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
          test_models + '/get_subscript_3d_arrays_xls/'
          + 'test_get_subscript_3d_arrays_xls.mdl'
        )
        assert_frames_close(output, canon, rtol=rtol)

    def test_get_xls_cellrange(self):
        output, canon = runner(
          test_models + '/get_xls_cellrange/'
          + 'test_get_xls_cellrange.mdl'
        )
        assert_frames_close(output, canon, rtol=rtol)

    def test_if_stmt(self):
        output, canon = runner(test_models + '/if_stmt/if_stmt.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_initial_function(self):
        output, canon = runner(test_models + '/initial_function/test_initial.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_input_functions(self):
        output, canon = runner(test_models + '/input_functions/test_inputs.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscripted_round(self):
        output, canon = runner(test_models + '/subscripted_round/test_subscripted_round.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_invert_matrix(self):
        output, canon = runner(test_models + '/invert_matrix/test_invert_matrix.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_limits(self):
        output, canon = runner(test_models + '/limits/test_limits.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_line_breaks(self):
        output, canon = runner(test_models + '/line_breaks/test_line_breaks.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_line_continuation(self):
        output, canon = runner(test_models + '/line_continuation/test_line_continuation.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_ln(self):
        output, canon = runner(test_models + '/ln/test_ln.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_log(self):
        output, canon = runner(test_models + '/log/test_log.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_logicals(self):
        output, canon = runner(test_models + '/logicals/test_logicals.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_lookups(self):
        output, canon = runner(test_models + '/lookups/test_lookups.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_lookups_without_range(self):
        output, canon = runner(test_models + '/lookups_without_range/test_lookups_without_range.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_lookups_funcnames(self):
        output, canon = runner(test_models + '/lookups_funcnames/test_lookups_funcnames.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_lookups_inline(self):
        output, canon = runner(test_models + '/lookups_inline/test_lookups_inline.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_lookups_inline_bounded(self):
        output, canon = runner(test_models + '/lookups_inline_bounded/test_lookups_inline_bounded.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_lookups_with_expr(self):
        output, canon = runner(test_models + '/lookups_with_expr/test_lookups_with_expr.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_macro_cross_reference(self):
        output, canon = runner(test_models + '/macro_cross_reference/test_macro_cross_reference.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_macro_expression(self):
        output, canon = runner(test_models + '/macro_expression/test_macro_expression.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_macro_multi_expression(self):
        output, canon = runner(test_models + '/macro_multi_expression/test_macro_multi_expression.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_macro_multi_macros(self):
        output, canon = runner(test_models + '/macro_multi_macros/test_macro_multi_macros.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    @unittest.skip('working')
    def test_macro_output(self):
        output, canon = runner(test_models + '/macro_output/test_macro_output.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_macro_stock(self):
        output, canon = runner(test_models + '/macro_stock/test_macro_stock.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    @unittest.skip('do we need this?')
    def test_macro_trailing_definition(self):
        output, canon = runner(test_models + '/macro_trailing_definition/test_macro_trailing_definition.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_model_doc(self):
        output, canon = runner(test_models + '/model_doc/model_doc.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_nested_functions(self):
        output, canon = runner(test_models + '/nested_functions/test_nested_functions.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_number_handling(self):
        output, canon = runner(test_models + '/number_handling/test_number_handling.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_parentheses(self):
        output, canon = runner(test_models + '/parentheses/test_parens.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    @unittest.skip('low priority')
    def test_reference_capitalization(self):
        """A properly formatted Vensim model should never create this failure"""
        output, canon = runner(test_models + '/reference_capitalization/test_reference_capitalization.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_repeated_subscript(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            output, canon = runner(test_models + '/repeated_subscript/test_repeated_subscript.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_rounding(self):
        output, canon = runner(test_models + '/rounding/test_rounding.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_sample_if_true(self):
        output, canon = runner(test_models + '/sample_if_true/test_sample_if_true.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_smooth(self):
        output, canon = runner(test_models + '/smooth/test_smooth.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_smooth_and_stock(self):
        output, canon = runner(test_models + '/smooth_and_stock/test_smooth_and_stock.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_special_characters(self):
        output, canon = runner(test_models + '/special_characters/test_special_variable_names.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_sqrt(self):
        output, canon = runner(test_models + '/sqrt/test_sqrt.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subrange_merge(self):
        output, canon = runner(test_models + '/subrange_merge/test_subrange_merge.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_logicals(self):
        output, canon = runner(test_models + '/subscript_logicals/test_subscript_logicals.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_multiples(self):
        output, canon = runner(test_models + '/subscript_multiples/test_multiple_subscripts.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_1d_arrays(self):
        output, canon = runner(test_models + '/subscript_1d_arrays/test_subscript_1d_arrays.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_2d_arrays(self):
        output, canon = runner(test_models + '/subscript_2d_arrays/test_subscript_2d_arrays.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_3d_arrays(self):
        output, canon = runner(test_models + '/subscript_3d_arrays/test_subscript_3d_arrays.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_3d_arrays_lengthwise(self):
        output, canon = runner(test_models + '/subscript_3d_arrays_lengthwise/test_subscript_3d_arrays_lengthwise.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_3d_arrays_widthwise(self):
        output, canon = runner(test_models + '/subscript_3d_arrays_widthwise/test_subscript_3d_arrays_widthwise.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_aggregation(self):
        output, canon = runner(test_models + '/subscript_aggregation/test_subscript_aggregation.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_constant_call(self):
        output, canon = runner(test_models + '/subscript_constant_call/test_subscript_constant_call.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_copy(self):
        output, canon = runner(test_models + '/subscript_copy/test_subscript_copy.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_docs(self):
        output, canon = runner(test_models + '/subscript_docs/subscript_docs.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_element_name(self):
        # issue https://github.com/JamesPHoughton/pysd/issues/216
        output, canon = runner(test_models + '/subscript_element_name/test_subscript_element_name.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_individually_defined_1_of_2d_arrays(self):
        output, canon = runner(test_models + '/subscript_individually_defined_1_of_2d_arrays/subscript_individually_defined_1_of_2d_arrays.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_individually_defined_1_of_2d_arrays_from_floats(self):
        output, canon = runner(test_models + '/subscript_individually_defined_1_of_2d_arrays_from_floats/subscript_individually_defined_1_of_2d_arrays_from_floats.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_individually_defined_1d_arrays(self):
        output, canon = runner(test_models + '/subscript_individually_defined_1d_arrays/subscript_individually_defined_1d_arrays.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_individually_defined_stocks(self):
        output, canon = runner(test_models + '/subscript_individually_defined_stocks/test_subscript_individually_defined_stocks.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_mapping_simple(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            output, canon = runner(test_models + '/subscript_mapping_simple/test_subscript_mapping_simple.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_mapping_vensim(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            output, canon = runner(test_models + '/subscript_mapping_vensim/test_subscript_mapping_vensim.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_mixed_assembly(self):
        output, canon = runner(test_models + '/subscript_mixed_assembly/test_subscript_mixed_assembly.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_selection(self):
        output, canon = runner(test_models + '/subscript_selection/subscript_selection.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_numeric_range(self):
        output, canon = runner(test_models + '/subscript_numeric_range/test_subscript_numeric_range.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_subranges(self):
        output, canon = runner(test_models + '/subscript_subranges/test_subscript_subrange.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_subranges_equal(self):
        output, canon = runner(test_models + '/subscript_subranges_equal/test_subscript_subrange_equal.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_switching(self):
        output, canon = runner(test_models + '/subscript_switching/subscript_switching.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_transposition(self):
        output, canon = runner(test_models + '/subscript_transposition/test_subscript_transposition.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscript_updimensioning(self):
        output, canon = runner(test_models + '/subscript_updimensioning/test_subscript_updimensioning.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscripted_delays(self):
        output, canon = runner(test_models + '/subscripted_delays/test_subscripted_delays.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscripted_flows(self):
        output, canon = runner(test_models + '/subscripted_flows/test_subscripted_flows.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscripted_if_then_else(self):
        output, canon = runner(test_models + '/subscripted_if_then_else/test_subscripted_if_then_else.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscripted_logicals(self):
        output, canon = runner(test_models + '/subscripted_logicals/test_subscripted_logicals.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscripted_smooth(self):
        # issue https://github.com/JamesPHoughton/pysd/issues/226
        output, canon = runner(test_models + '/subscripted_smooth/test_subscripted_smooth.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscripted_trend(self):
        # issue https://github.com/JamesPHoughton/pysd/issues/226
        output, canon = runner(test_models + '/subscripted_trend/test_subscripted_trend.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subscripted_xidz(self):
        output, canon = runner(test_models + '/subscripted_xidz/test_subscripted_xidz.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_subset_duplicated_coord(self):
        output, canon = runner(test_models + '/subset_duplicated_coord/'
                               + 'test_subset_duplicated_coord.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_time(self):
        output, canon = runner(test_models + '/time/test_time.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_trend(self):
        output, canon = runner(test_models + '/trend/test_trend.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_trig(self):
        output, canon = runner(test_models + '/trig/test_trig.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_variable_ranges(self):
        output, canon = runner(test_models + '/variable_ranges/test_variable_ranges.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_unicode_characters(self):
        output, canon = runner(test_models + '/unicode_characters/unicode_test_model.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_xidz_zidz(self):
        output, canon = runner(test_models + '/xidz_zidz/xidz_zidz.mdl')
        assert_frames_close(output, canon, rtol=rtol)

    def test_run_uppercase(self):
        output, canon = runner(test_models + '/case_sensitive_extension/teacup-upper.MDL')
        assert_frames_close(output, canon, rtol=rtol)

    def test_odd_number_quotes(self):
        output, canon = runner(test_models + '/odd_number_quotes/teacup_3quotes.mdl')
        assert_frames_close(output, canon, rtol=rtol)
