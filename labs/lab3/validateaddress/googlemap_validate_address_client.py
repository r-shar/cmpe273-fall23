import grpc
import logging

import address_validation_pb2
import address_validation_pb2_grpc

def run():
    print("Will try to validate address...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = address_validation_pb2_grpc.AddressValidationStub(channel)
        response = stub.ValidateAddress(address_validation_pb2.ValidateAddressRequest(
            address="1 Washington Sq, San Jose, CA 95192"
        ))
        print(f'Address validation client received {response.message}')

if __name__ == "__main__":
    logging.basicConfig()
    run()