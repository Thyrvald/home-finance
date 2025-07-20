import { useState } from "react";
import { ListOneTimeExpenses } from "../../components/Expenses/ListOneTimeExpenses.tsx";

export default function ListOneTimeExpensesPage() {
    const [reload, setReload] = useState(false);

    return (
        <div>
            <h1 className="text-2xl font-bold mb-4">Lista Wydatków</h1>
            <ListOneTimeExpenses reload={reload} />
        </div>
    );
}