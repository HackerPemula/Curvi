from models.document_model import Document
from services.helper import exception

class DocumentService():
    @staticmethod
    @exception
    def get_all_documents():
        results = Document.objects.exec_sp_tolist('jh_Document_GetAllDocuments')

        documents = []
        for result in results:
            documents.append(Document(DocumentID=result[0], Title=result[1], Description=result[2], RegistrantID=result[3], DocumentUrl=result[4], StatusRecord=[5]))

        return documents

    @staticmethod
    @exception
    def save_documents():
        results = Document.objects.exec_sp_tolist(
            'jh_Document_SaveDocuments')

        documents = []
        for result in results:
            documents.append(Document(DocumentID=result[0], Title=result[1], Description=result[2], RegistrantID=result[3], DocumentUrl=result[4], StatusRecord=[5]))

        return documents
