import { useState } from "react";
import { GetBalance } from "../components/GetBalance";

export default function ListIncomePage() {
    const [reload, setReload] = useState(false);

    return (
        <div>
            <h1 className="text-2xl font-bold mb-4">Bilans</h1>
            <GetBalance reload={reload} />
        </div>
    );
}