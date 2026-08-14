class User:
    def __init__(self, user_id: int, name: str, email: str, role: str):
        self.id = user_id
        self.name = name
        self.email = email
        self.role = role

    def login((self) -> bool:
        """Simula el inicio de sesion de un usuario."""
        return True

    def __str__(self):
        return f"User({self.id}, {self.name}, {self.role})"


class Comment:
    def __init__(self, comment_id: int, content: str, author: User, created_at: str):
        self.id = comment_id
        self.content = content
        self.author = author
        self.created_at = created_at

    def get_summary(self) -> str:
        return f"Comentario por {self.author.name}: {self.content[:30]}..."


class History:
    def __init__(self, history_id: int, action: str, timestamp: str):
        self.id = history_id
        self.action = action
        self.timestamp = timestamp

    def log_entry(self) -> str:
        return f"[{self.timestamp}] Accion: {self.action}"


class Ticket:
    def __init__(self, ticket_id: int, title: str, description: str, priority: str, requester: User):
        self.id = ticket_id
        self.title = title
        self.description = description
        self.priority = priority
        self.requester = requester  
        self.technician = None      
        self._status = "Open"
        self.comments = []          
        self.history = []           

    def assign_technician(self, tech: User) -> None:
        if tech.role.lower() == "technician":
            self.technician = tech
            self.history.append(History(len(self.history) + 1, f"Tecnico {tech.name} asignado", "2026-03-01"))
        else:
            print(f"[ERROR] El usuario {tech.name} no posee rol de tecnico.")

    def change_status(self, new_status: str) -> None:
        self._status = new_status
        self.history.append(History(len(self.history) + 1, f"Estado cambiado a {new_status}", "2026-03-01"))

    def add_comment(self, content: str, author: User) -> None:
        new_comment = Comment(len(self.comments) + 1, content, author, "2026-03-01")
        self.comments.append(new_comment)


class Article:
    def __init__(self, article_id: int, title: str, content: str, author: User):
        self.id = article_id
        self.title = title
        self.content = content
        self.author = author  

    def publish(self) -> None:
        print(f"[INFO] Articulo '{self.title}' publicado por {self.author.name}.")