import { Player } from "./player";

export interface Form {
    id: string;
    player: Player,

    rating: number,
    match_description: string,
    comment: string,
    created_at: string
}
