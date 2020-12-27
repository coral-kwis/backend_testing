from assertpy import assert_that


class TestBase(object):

    @staticmethod
    def assert_string_equal(actual_value, expected_value):
        assert_that(actual_value,
                    f'Expected value is {expected_value}'
                    f'. But got actual value is {actual_value}'
                    ).is_equal_to(expected_value)

    @staticmethod
    def assert_list_equal(actual_value, expected_value):
        assert_that(set(actual_value),
                    f'Expected list is {expected_value}'
                    f'. But got actual list is {actual_value}'
                    ).is_equal_to(set(expected_value))

    @staticmethod
    def assert_true(actual_value):
        assert_that(actual_value,
                    f'Expected value is True. But got actual value is {actual_value}'
                    ).is_true()

    @staticmethod
    def assert_false(actual_value):
        assert_that(actual_value,
                    f'Expected value is True. But got actual value is {actual_value}'
                    ).is_false()
