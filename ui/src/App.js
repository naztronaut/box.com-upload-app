import React from "react";
import logo from "./logo.svg";
import "./App.css";
import Header from "./components/header";
import BoxUpload from "./components/upload";
import "primeicons/primeicons.css";
import "bootstrap/dist/css/bootstrap.css";
import "primereact/resources/primereact.css";
import "primereact/resources/themes/luna-pink/theme.css";

function App() {
  return (
    <div className="App">
      <Header />
      <BoxUpload />
    </div>
  );
}

export default App;
