import grpc
from concurrent import futures
import logging

import address_validation_pb2_grpc
import address_validation_pb2

class AddressValidation(address_validation_pb2_grpc.AddressValidationServicer):
    def ValidateAddress(self, request, context):
        return address_validation_pb2.ValidateAddressResponse(message=request.address)
    

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    address_validation_pb2_grpc.add_AddressValidationServicer_to_server(AddressValidation(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print(f'Server started, listening on port {port}')
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()