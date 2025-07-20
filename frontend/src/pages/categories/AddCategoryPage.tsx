import {useState} from "react";

export default function AddCategoryPage() {
    const [reload, setReload] = useState(false);

    return (
        <div>
            <h1 className="text-2xl font-bold mb-4">Kategorie</h1>
            <p>Tu będzie dodawanie kategorii.</p>
        </div>
    );
}