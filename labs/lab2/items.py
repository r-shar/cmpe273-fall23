import strawberry

# for this assignment, using data structure to store items
# in more complex use case, would use data store

global items_dict
items_dict = { }


@strawberry.type
class Item:
    id: int
    name: str

def get_item(id:int):
    return items_dict[id] if items_dict else None

@strawberry.type
class Query:

    @strawberry.field
    def get_item_by_id(self, id:int) -> Item:
        item = items_dict[id]
        return item

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_item(self, id:int, name:str) -> Item:
        print(f"Adding item {name} with id {id}")

        created_item = Item(id=id, name=name)
        if (id not in items_dict):
            items_dict[id] = created_item

        return created_item
    
    @strawberry.mutation
    def update_item(self, id:int, newName:str) -> Item:
        print(f"Updating item with id: {id} to have name: {newName}")

        item = get_item(id)
        item.name = newName
        items_dict[id] = item

        return item
    
    @strawberry.mutation
    def delete_item(self, id:int) -> None:
        print(f'Deleting item with id: {id}')
        items_dict.pop(id)
    


schema = strawberry.Schema(query=Query, mutation=Mutation)
