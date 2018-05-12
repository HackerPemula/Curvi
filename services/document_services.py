from models.document_model import Document
from services.helper import exception

class DocumentService():
    @staticmethod
    @exception
    def get_all_documents():
        results = Document.objects.exec_sp_tolist('jh_Document_GetAllDocuments')

        documents = []
        for result in results:
            documents.append(Document(DocumentID=result[0], Title=result[1], Content=result[2], RegistrantID=result[3], DocumentUrl=result[4], StatusRecord=result[5]))

        return documents

    @staticmethod
    @exception
    def get_document_by_id(param):
        result = Document.objects.exec_sp_tosingle('jh_Document_GetDocumentsByID', param)
        document = Document(DocumentID=result[0], Title=result[1], Content=result[2], RegistrantID=result[3], DocumentUrl=result[4], StatusRecord=result[5], CategoryID=result[6])
        return document

    @staticmethod
    @exception
    def update_document_category_by_id(param):
        result = Document.objects.exec_sp('jh_Document_UpdateDocumentCategoryByID', param)
        return result

    @staticmethod
    @exception
    def save_documents(param):
        result = Document.objects.exec_sp_tosingle('jh_Document_SaveDocuments', param)

        documents = Document(DocumentID=result[0], Title=result[1], Content=result[2], RegistrantID=result[3], DocumentUrl=result[4], StatusRecord=[5], CategoryID=result[6])

        return documents
