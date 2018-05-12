from models.preprocessed_document_model import PreprocessedDocument
from services.helper import exception

class PreprocessedDocumentService():
    # @staticmethod
    # @exception
    # def get_preprocessed_document(param):
    #     results = Topic.objects.exec_sp_tolist('jh_Topic_GetTopic', param)

    #     topic = []
    #     for result in results:
    #         topic.append(Topic(TopicID=result[0], EnglishTopic=result[1], IndonesianTopic=result[2]))

    #     return topic

    @staticmethod
    @exception
    def insert_preprocessed_document(param):
        result = PreprocessedDocument.objects.exec_sp_tosingle('jh_Topic_InsertPreprocessedDocument', param)

        preprocessed_document = None
        if result:
            preprocessed_document = PreprocessedDocument(PreprocessedID=result[0], DocumentID=result[1], Token=result[2], Stemmed=result[3])

        return preprocessed_document