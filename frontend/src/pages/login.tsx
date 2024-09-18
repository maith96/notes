import { FormEvent, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import api from "../api";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import { Button, Input } from "@nextui-org/react";
import { Card, CardBody, CardFooter } from "@nextui-org/card";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setIsLoading] = useState(false);

  const navigate = useNavigate();

  const handleSubmit = async (event: FormEvent<HTMLFormElement>) => {
    setIsLoading(true);
    event.preventDefault();

    try {
      const res = await api.post("/api/token/", {
        email,
        password,
      });

      localStorage.setItem(ACCESS_TOKEN, res.data.access);
      localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
      console.log(res);

      navigate("/");
    } catch (error) {
      alert(error);
    } finally {
      setIsLoading(false);
    }

    // Call API to authenticate user
    // ...
  };
  return (
    <div>
      <Card className="max-w-md mx-auto mt-10">
        <CardBody>
          <form onSubmit={handleSubmit} className=" flex flex-col gap-4">
            <h1 className="text-2xl text-center font-bold mb-10">Login</h1>
            <Input
              type="email"
              label="email"
              placeholder="Enter your email"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
            />
            <Input
              type="password"
              label="Password"
              placeholder="Enter your password"
              value={password}
              onChange={(event) => setPassword(event.target.value)}
            />
            <Button color="primary" type="submit">
              Login
            </Button>
            {error && <div style={{ color: "red" }}>{error}</div>}
          </form>
        </CardBody>
        <CardFooter>
          <p>
            Don't have an account?{" "}
            <Link className="text-primary" to="/register">
              create account.
            </Link>
          </p>
        </CardFooter>
      </Card>
    </div>
  );
}
