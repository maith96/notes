import {
  Button,
  Card,
  CardBody,
  CardFooter,
  CardHeader,
} from "@nextui-org/react";

function Note({ note, onDelete }) {
  const formattedDate = new Date(note.updated_at).toLocaleDateString("en-US");
  console.log(note);

  return (
    <Card className="max-w-md min-w-[250px]">
      <CardHeader className="flex flex-col items-start">
        <p className="text-md">{note.title}</p>
        <small className="text-default-500">{formattedDate}</small>
      </CardHeader>
      <CardBody>
        {" "}
        <p className="note-content">{note.content}</p>
      </CardBody>
      <CardFooter className="flex justify-end">
        <Button color="danger" onClick={() => onDelete(note.id)}>
          Delete
        </Button>
      </CardFooter>
    </Card>
  );
}

export default Note;
