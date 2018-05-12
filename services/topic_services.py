from models.topic_model import Topic
from services.helper import exception

class TopicService():
    @staticmethod
    @exception
    def get_topic(param):
        results = Topic.objects.exec_sp_tolist('jh_Topic_GetTopic', param)

        topic = []
        for result in results:
            topic.append(Topic(TopicID=result[0], EnglishTopic=result[1], IndonesianTopic=result[2]))

        return topic

    @staticmethod
    @exception
    def insert_topic(param):
        results = Topic.objects.exec_sp_tosingle('jh_Topic_InsertTopic', param)

        topic = []
        for result in results:
            topic.append(Topic(TopicID=result[0], EnglishTopic=result[1], IndonesianTopic=result[2]))

        return topic