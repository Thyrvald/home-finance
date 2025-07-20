import { AddOneTimeExpenseForm } from "../../components/Expenses/AddOneTimeExpenseForm.tsx";

export default function AddOneTimeExpensePage() {
    return (
        <div>
            <h1 className="text-2xl font-bold mb-4">Dodaj wydatek</h1>
            <AddOneTimeExpenseForm onAdd={() => {}} />
        </div>
    );
}