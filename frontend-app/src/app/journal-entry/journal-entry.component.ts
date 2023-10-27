import { Component, Input } from '@angular/core';
import { PostDetail } from '../postdetail';

@Component({
  selector: 'app-journal-entry',
  templateUrl: './journal-entry.component.html',
  styleUrls: ['./journal-entry.component.css'],
  standalone: true
})

export class JournalEntryComponent {
  @Input() entryDetail!: PostDetail;
}

