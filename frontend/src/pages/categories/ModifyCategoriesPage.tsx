import {useState} from "react";

export default function ModifyCategoryPage() {
    const [reload, setReload] = useState(false);

    return (
        <div>
            <h1 className="text-2xl font-bold mb-4">Kategorie</h1>
            <p>Tu będzie modyfikowanie kategorii.</p>
        </div>
    );
}