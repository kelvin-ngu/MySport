import { Player } from "./player";

export interface Form {
    title: string;
    player: Player,
    public: boolean,
    feelings: string,
    entry: string,
    get_up: string
}