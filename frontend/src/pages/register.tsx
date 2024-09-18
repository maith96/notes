import { FormEvent, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import api from "../api";
import { Button, Input } from "@nextui-org/react";
import { Card, CardBody, CardFooter } from "@nextui-org/card";

export default function Register() {
  localStorage.clear();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const [loading, setIsLoading] = useState(false);

  const navigate = useNavigate();

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    setIsLoading(true);
    event.preventDefault();

    try {
      await api.post("/api/user/register/", {
        username,
        password,
      });
      navigate("/login");
    } catch (error) {
      alert(error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      <Card className="max-w-md mx-auto mt-10">
        <CardBody>
          <form onSubmit={handleSubmit} className=" flex flex-col gap-4">
            <h1 className="text-2xl text-center font-bold mb-10">Register</h1>
            <Input
              type="username"
              label="Username"
              placeholder="Enter your username"
              value={username}
              onChange={(event) => setUsername(event.target.value)}
            />
            <Input
              type="password"
              label="Password"
              placeholder="Enter your password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
            />
            <Button color="primary" type="submit">
              Create Account
            </Button>
            {error && <div style={{ color: "red" }}>{error}</div>}
          </form>
        </CardBody>
        <CardFooter>
          <p>
            Already have an account?{" "}
            <Link className="text-primary" to="/login">
              Log in.
            </Link>
          </p>
        </CardFooter>
      </Card>
    </div>
  );
}
