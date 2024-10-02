import grpc
from concurrent import futures
import crud_pb2
import crud_pb2_grpc
from database import Database

class CRUDService(crud_pb2_grpc.CRUDServiceServicer):
    def __init__(self):
        self.db = Database()

    def Create(self, request, context):
        item_id = self.db.insert_item(request.name)
        return crud_pb2.Response(message=f'Item created with ID {item_id}')

    def Read(self, request, context):
        item = self.db.get_item(request.id)
        if item:
            return crud_pb2.Item(id=item[0], name=item[1])
        context.set_code(grpc.StatusCode.NOT_FOUND)
        context.set_details(f'Item with ID {request.id} not found')
        return crud_pb2.Item()

    def Update(self, request, context):
        self.db.update_item(request.id, request.name)
        return crud_pb2.Response(message='Item updated successfully')

    def Delete(self, request, context):
        self.db.delete_item(request.id)
        return crud_pb2.Response(message='Item deleted successfully')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    crud_pb2_grpc.add_CRUDServiceServicer_to_server(CRUDService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()