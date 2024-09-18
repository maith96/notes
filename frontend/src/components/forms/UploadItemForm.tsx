// components/UploadItemForm.js
import { useState } from "react";
import {
  Input,
  Textarea,
  Button,
  Select,
  Spacer,
  SelectItem,
} from "@nextui-org/react";
import { ITEM_TYPES } from "../../constants";
import api from "../../api";

const UploadItemForm = () => {
  const [itemType, setItemType] = useState("school_id");
  const [identifier, setIdentifier] = useState("");
  const [description, setDescription] = useState("");
  const [photo, setPhoto] = useState(null);

  const handlePhotoChange = (e) => {
    setPhoto(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("identifier", identifier);
    formData.append("description", description);
    formData.append("photo", photo);
    formData.append("item_type", itemType);

    const response = await api.post(`/api/items/create/`, formData, {
      headers: {
        "Content-Type": "multipart/form-data", // Optional, Axios sets this automatically for FormData
      },
    });

    if (response.ok) {
      alert("Item uploaded successfully!");
    } else {
      alert("Failed to upload item.");
    }
  };

  const requestSTKPush = async () => {
    const res = await api.post("/api/transactions/request_stk_push", {
      initiated_by: "c4269cd7-70d7-4777-949e-4d23c161f6b9",
      item_type: "national_id",
      item_id: "3c778ccf-3420-4f78-83de-3362d11bf5e0",
      amount: "1",
      phone_number: "254710726252",
    });
  };
  return (
    <form
      onSubmit={handleSubmit}
      className="max-w-md m-auto flex flex-col gap-5"
    >
      <Select
        label="Item Type"
        placeholder="Select item type"
        className=""
        value={itemType}
        onChange={(e) => setItemType(e.target.value)}
      >
        {ITEM_TYPES.map((item) => (
          <SelectItem key={item.key}>{item.label}</SelectItem>
        ))}
      </Select>

      <Input
        label="Identifier"
        placeholder="Enter the identifier"
        value={identifier}
        onChange={(e) => setIdentifier(e.target.value)}
        required
      />

      <Textarea
        label="Description"
        placeholder="Enter a brief description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
        required
      />

      <Input
        label="Upload Photo"
        type="file"
        onChange={handlePhotoChange}
        required
      />

      <Button type="submit" color="primary" className="primary">
        Upload Item
      </Button>

      <Button color="primary" className="primary" onClick={requestSTKPush}>
        Test Paymen
      </Button>
    </form>
  );
};

export default UploadItemForm;
