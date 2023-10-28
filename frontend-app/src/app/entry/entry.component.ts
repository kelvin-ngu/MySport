import { Component, Input } from '@angular/core';
import { FormList } from '../formList';
@Component({
  selector: 'app-entry',
  templateUrl: './entry.component.html',
  styleUrls: ['./entry.component.css']
})
export class EntryComponent {
    @Input()
  formList!: FormList;
}

