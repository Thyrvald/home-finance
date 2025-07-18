import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Layout from "./components/Layout";
import AddIncomePage from "./pages/income/AddIncomePage";
import ListIncomePage from "./pages/income/ListIncomePage";
import BalancePage from "./pages/BalancePage";
import AddOneTimeExpensePage from "./pages/one-time-expenses/AddOneTimeExpensePage";
import ListOneTimeExpensesPage from "./pages/one-time-expenses/ListOneTimeExpensesPage";

function App() {
    return (
        <Router>
            <Layout>
                <Routes>
                    <Route path="/" element={<Navigate to="/income/add" />} />
                    <Route path="/income/add" element={<AddIncomePage />} />
                    <Route path="/income/list" element={<ListIncomePage />} />
                    <Route path="/one-time-expenses/add" element={<AddOneTimeExpensePage />} />
                    <Route path="/one-time-expenses/list" element={<ListOneTimeExpensesPage />} />
                    <Route path="/balance" element={<BalancePage />} />
                </Routes>
            </Layout>
        </Router>
    );
}

export default App;