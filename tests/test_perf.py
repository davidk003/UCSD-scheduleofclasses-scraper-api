# """
# Performance tests for the UCSD Schedule API.
# """

# import pprint
# from ucsd_schedule_api.core import UCSDClassScheduleAPI


# class TestPerf:
#     # def test_get_terms(self):
#     #     api = UCSDClassScheduleAPI()
#     #     result = api.get_terms()
#     #     print("\n" + "**************".center(40, "*"))
#     #     print(len(result))
#     #     pprint.pprint(result)
#     #     print("**************".center(40, "*"))

#     # def test_get_subject_list(self):
#     #     api = UCSDClassScheduleAPI()
#     #     result = api.get_subject_list("FA25")
#     #     print("\n" + "**************".center(40, "*"))
#     #     print(len(result))
#     #     pprint.pprint(result)
#     #     print("**************".center(40, "*"))

#     # def test_get_departments(self):
#     #     api = UCSDClassScheduleAPI()
#     #     result = api.get_departments("FA25")
#     #     print("\n" + "**************".center(40, "*"))
#     #     print(len(result))
#     #     pprint.pprint(result)
#     #     print("**************".center(40, "*"))

#     def test_get_schedule_search_form(self):
#         api = UCSDClassScheduleAPI()
#         result = api._get_schedule_form_inputs()
#         print("\n" + "**************".center(40, "*"))
#         pprint.pprint(result)
#         print("**************".center(40, "*"))
    
#     def test_search_schedule(self):
#         api = UCSDClassScheduleAPI()
#         result = api.get_schedule_page_by_term_subject("FA25", ["ECE", "CSE"])
#         print("\n" + "**************".center(40, "*"))
#         # print(result)
#         pprint.pprint(api._get_schedule_form_inputs())
#         print("**************".center(40, "*"))