import { useState } from "react";
import { Input, Button, Select, SelectItem } from "@nextui-org/react";
import { ITEM_TYPES } from "../../constants";
import api from "../../api";

export default function SearchForm() {
  const [itemType, setItemType] = useState("school_id");
  const [identifier, setIdentifier] = useState("");
  const [foundItem, setFoundItem] = useState([]);
  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("identifier", identifier);
    formData.append("item_type", itemType);

    const response = await api.post(`/api/items/search/`, formData, {
      headers: {
        "Content-Type": "multipart/form-data", // Optional, Axios sets this automatically for FormData
      },
    });

    if (response.ok) {
      alert("Item uploaded successfully!");
    } else {
      console.log(response.data);
      setFoundItem(response.data);
    }
  };

  const get_balance = () => {
    // api
    //   .get(`/api/account/user/balance/`)
    //   .then((res) => res.data)
    //   .then((data) => {
    //     console.log(data);
    //     setFoundItem(data);
    //   });
  };

  const claim = async (id: string, item_type: string) => {
    const res = await api.post("/api/payment/make-payment/", {
      item_id: id,
      item_type: item_type,
      phone_number: 254748075877,
    });
    console.log(res);
  };
  return (
    <div>
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

        <Button type="submit" color="primary" className="primary">
          Find Item
        </Button>
        <Button
          color="danger"
          className="primary"
          onPress={() => get_balance()}
        >
          get balance
        </Button>
      </form>

      <div>
        {foundItem.map((item) => (
          <>
            <div key={item.id}>
              <p>{item?.id}</p>
              <p>{item?.item_type}</p>
            </div>
            <div>
              <Button
                onPress={() => claim(item.id, item.item_type)}
                color="primary"
                className="primary"
              >
                Claim Item
              </Button>
            </div>
          </>
        ))}
      </div>
    </div>
  );
}
