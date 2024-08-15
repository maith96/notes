import { FormEvent, useEffect, useState } from "react";
import api from "../api";
import Note from "../components/Note";
import { Divider } from "@nextui-org/react";

export default function Home() {
  const [notes, setNotes] = useState([]);
  const [content, setContent] = useState("");
  const [title, setTitle] = useState("");

  useEffect(() => {
    getNotes();
  }, []);
  const getNotes = () => {
    api
      .get("/api/notes/")
      .then((res) => res.data)
      .then((data) => setNotes(data))
      .catch((err) => alert(err));
  };

  const deleteNote = (id: number) => {
    api
      .delete(`/api/notes/delete/${id}`)
      .then((res) => {
        if (res.status === 204) {
          alert("Note deleted");
          getNotes();
        } else alert("Failed to delete Note");
      })
      .catch((e) => alert(e));
  };

  const createNote = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    api
      .post("/api/notes/", {
        title,
        content,
      })
      .then((res) => {
        if (res.status === 201) {
          alert("Note created");
          getNotes();
        } else alert("Failed to create Note");
      })
      .catch((e) => alert(e));
  };
  return (
    <>
      <div className="p-5">
        <h2 className="text-xl pl-2">Notes</h2>
        <Divider className="my-2" />
        <div className="flex flex-wrap gap-4">
          {notes.map((note) => (
            <Note note={note} onDelete={deleteNote} />
          ))}
        </div>

        <h2>Create Note</h2>
        <form onSubmit={createNote}>
          <label>
            Title:
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
            />
          </label>
          <br />
          <label>
            Content:
            <input
              type="text"
              value={content}
              onChange={(e) => setContent(e.target.value)}
            />
          </label>
          <br />
          <button type="submit">Create Note</button>
        </form>
      </div>
    </>
  );
}
