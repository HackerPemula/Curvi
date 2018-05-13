from models.topic_result_model import TopicResult
from services.helper import exception

class TopicResultService():
    # @staticmethod
    # @exception
    # def get_topic(param):
    #     results = Topic.objects.exec_sp_tolist('jh_Topic_GetTopic', param)

    #     topic = []
    #     for result in results:
    #         topic.append(Topic(TopicID=result[0], EnglishTopic=result[1], IndonesianTopic=result[2]))

    #     return topic

    @staticmethod
    @exception
    def insert_topic_result(param):
        results = TopicResult.objects.exec_sp('jh_Topic_InsertTopicResult', param)

        return results