import { AddIncomeForm } from "../../components/Income/AddIncomeForm.tsx";

export default function AddIncomePage() {
    return (
        <div>
            <h1 className="text-2xl font-bold mb-4">Dodaj przychód</h1>
            <AddIncomeForm onAdd={() => {}} />
        </div>
    );
}