import { useState } from "react";
import { ListIncome } from "../../components/ListIncome";

export default function ListIncomePage() {
    const [reload, setReload] = useState(false);

    return (
        <div>
            <h1 className="text-2xl font-bold mb-4">Lista przychodów</h1>
            <ListIncome reload={reload} />
        </div>
    );
}