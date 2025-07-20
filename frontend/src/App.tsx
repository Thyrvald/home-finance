import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Layout from "./components/Shared/Layout.tsx";
import AddCategoryPage from "./pages/categories/AddCategoryPage";
import ModifyCategoryPage from "./pages/categories/AddCategoryPage";
import AddIncomePage from "./pages/income/AddIncomePage";
import ListIncomePage from "./pages/income/ListIncomePage";
import BalancePage from "./pages/BalancePage";
import AddOneTimeExpensePage from "./pages/expenses/one-time-expenses/AddOneTimeExpensePage";
import ListOneTimeExpensesPage from "./pages/expenses/one-time-expenses/ListOneTimeExpensesPage";

function App() {
    return (
        <Router>
            <Layout>
                <Routes>
                    <Route path="/" element={<Navigate to="/income/add" />} />
                    <Route path="/categories/add" element={<AddCategoryPage />} />
                    <Route path="/categories/modify" element={<ModifyCategoryPage />} />
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