import { Component } from '@angular/core';
import { JournalEntryComponent } from '../journal-entry/journal-entry.component';

@Component({
  selector: 'app-mygame',
  templateUrl: './mygame.component.html',
  styleUrls: ['./mygame.component.css'],
  standalone: true,
  imports: [JournalEntryComponent]
})
export class MygameComponent {
  
}
