import { Player } from "./player";

export interface Form {
    id: string,
    public: boolean,
    player: Player,
    title: string,
    get_up: string,
    feelings: string,
    entry: string,
    created_at: string
}