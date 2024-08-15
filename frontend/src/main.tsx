import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.tsx";
import { NextUIProvider } from "@nextui-org/react";

import "./index.css";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <NextUIProvider>
      <main className="dark text-foreground bg-background h-[100vh]">
        <App />
      </main>
    </NextUIProvider>
  </StrictMode>
);
