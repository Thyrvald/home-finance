import { AddCategoryForm } from "../../components/Categories/AddCategoryForm.tsx";

export default function AddIncomePage() {
    return (
        <div>
            <h1 className="text-2xl font-bold mb-4">Dodaj kategorię</h1>
            <AddCategoryForm onAdd={() => {}} />
        </div>
    );
}