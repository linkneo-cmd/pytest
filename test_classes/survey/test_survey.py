import pytest
from survey import AnonymousSurvey

# def test_store_single_response():
#     question = "What language did you first learn to speak?"
#     lang_survey = AnonymousSurvey(question)
#     lang_survey.store_response('English')
#     assert 'English' in lang_survey.responses

# def test_store_three_responses():
#     question = "What language did you first learn to speak?"
#     lang_survey = AnonymousSurvey(question)
#     responses = ['English', 'Spanish', 'Mandarin']
#     for response in responses:
#         lang_survey.store_response(response)
#     for response in responses:
#         assert response in lang_survey.responses

@pytest.fixture
def lang_survey():
    "一个可供所有测试函数使用的AnonymousSurvey实例"
    question = "What language did you first learn to speak?"
    lang_survey = AnonymousSurvey(question)
    return lang_survey

# 当测试函数的一个形参与应用了装饰器@pytest.fixture的函数（夹具）同名时，将自动运行该夹具，并将其返回值传递给测试函数
def test_store_single_response(lang_survey):
    lang_survey.store_response('English')
    assert 'English' in lang_survey.responses

def test_store_three_responses(lang_survey):
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        lang_survey.store_response(response)
    for response in responses:
        assert response in lang_survey.responses