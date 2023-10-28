import { Player } from "./player"

export interface Form {
    id: string,
    player: Player,
    public: boolean,
    title: string,
    description: string,
    created_at: string
}
