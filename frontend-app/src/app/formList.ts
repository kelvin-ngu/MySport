import { Form } from "./form";
export interface FormList extends Iterable<Form> {
    formlist: Array<Form>;
}