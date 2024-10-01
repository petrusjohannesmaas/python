import tkinter as tk
from tkinter import messagebox
import grpc
import crud_pb2
import crud_pb2_grpc

class CRUDClientApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CRUD Client")

        self.stub = None
        self.connect_to_server()

        # UI Elements
        self.label = tk.Label(master, text="Item Name:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.create_button = tk.Button(master, text="Create", command=self.create_item)
        self.create_button.pack()

        self.read_button = tk.Button(master, text="Read", command=self.read_item)
        self.read_button.pack()

        self.update_button = tk.Button(master, text="Update", command=self.update_item)
        self.update_button.pack()

        self.delete_button = tk.Button(master, text="Delete", command=self.delete_item)
        self.delete_button.pack()

        self.id_entry = tk.Entry(master)
        self.id_entry.pack()
        self.id_entry.insert(0, "Enter ID here")

    def connect_to_server(self):
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = crud_pb2_grpc.CRUDServiceStub(channel)

    def create_item(self):
        name = self.entry.get()
        if name:
            response = self.stub.Create(crud_pb2.Item(name=name))
            messagebox.showinfo("Response", response.message)
        else:
            messagebox.showwarning("Input Error", "Please enter a name.")

    def read_item(self):
        item_id = self.id_entry.get()
        if item_id.isdigit():
            response = self.stub.Read(crud_pb2.ItemId(id=int(item_id)))
            messagebox.showinfo("Response", f"ID: {response.id}, Name: {response.name}")
        else:
            messagebox.showwarning("Input Error", "Please enter a valid ID.")

    def update_item(self):
        item_id = self.id_entry.get()
        name = self.entry.get()
        if item_id.isdigit() and name:
            response = self.stub.Update(crud_pb2.Item(id=int(item_id), name=name))
            messagebox.showinfo("Response", response.message)
        else:
            messagebox.showwarning("Input Error", "Please enter a valid ID and a name.")

    def delete_item(self):
        item_id = self.id_entry.get()
        if item_id.isdigit():
            response = self.stub.Delete(crud_pb2.ItemId(id=int(item_id)))
            messagebox.showinfo("Response", response.message)
        else:
            messagebox.showwarning("Input Error", "Please enter a valid ID.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CRUDClientApp(root)
    root.mainloop()
