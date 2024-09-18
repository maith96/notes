import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Register from "./pages/register";
import ProtectedRoute from "./components/ProtectedRoute";
import Home from "./pages/Home";
import Login from "./pages/login";
import NotFound from "./pages/NotFound";
import Header from "./components/Header";
import Report from "./pages/Report";
import api from "./api";
import Search from "./pages/Search";

function App() {
  function Logout() {
    localStorage.clear();
    return <Navigate to="/login" />;
  }

  const get_user = async () => {
    const user = await api.get("/api/account/");
  };
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
        <Route
          path="/report"
          element={
            <ProtectedRoute>
              <Report />
            </ProtectedRoute>
          }
        ></Route>

        <Route path="/login" element={<Login />}></Route>
        <Route path="/report" element={<Login />}></Route>
        <Route path="/logout" element={<Logout />}></Route>
        <Route path="/register" element={<Register />}></Route>
        <Route path="/search" element={<Search />}></Route>
        <Route path="*" element={<NotFound />}></Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
