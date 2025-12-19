import RuleList from "./components/RuleList";
import RuleForm from "./components/RuleForm";
import { useState } from "react";

function App () {
  const [refresh, setRefresh] = useState(false);
  return (
    <div className="container mx-auto">
      <h1 className="text-2xl font-bold my-4">Smart Poultry Rule Dashboard</h1>
      <RuleForm onSaved={() => setRefresh(!refresh)} />
      <RuleList key={refresh} />
    </div>
  );
}

export default App;
