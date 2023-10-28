import { Component } from '@angular/core';
import { EntryboxComponent } from '../entrybox/entrybox.component';


@Component({
  selector: 'app-new-entry',
  templateUrl: './new-entry.component.html',
  styleUrls: ['./new-entry.component.css'],
  standalone: true,
  imports: [EntryboxComponent]
})
export class NewEntryComponent {

}