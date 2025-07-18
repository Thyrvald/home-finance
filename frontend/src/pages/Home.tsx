import { useState } from "react";
import { AddIncomeForm } from "../components/AddIncomeForm";
import { ListIncome } from "../components/ListIncome.tsx";

export default function Home() {
    const [reload, setReload] = useState(false);

    const handleAdd = () => {
        console.log("Changing reload");
        setReload((prev) => !prev);
    };

    return (
        <div className="max-w-xl mx-auto mt-10">
            <h1 className="text-2xl font-bold mb-4">Przychody</h1>
            <AddIncomeForm onAdd={handleAdd} />
            <ListIncome reload={reload} />
        </div>
    );
}