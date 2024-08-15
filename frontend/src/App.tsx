import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Register from "./pages/register";
import ProtectedRoute from "./components/ProtectedRoute";
import Home from "./pages/Home";
import Login from "./pages/login";
import NotFound from "./pages/NotFound";
import Header from "./components/Header";

function App() {
  function Logout() {
    localStorage.clear();
    return <Navigate to="/login" />;
  }

  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          }
        ></Route>
        <Route path="/login" element={<Login />}></Route>
        <Route path="/logout" element={<Logout />}></Route>
        <Route path="/register" element={<Register />}></Route>
        <Route path="*" element={<NotFound />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
