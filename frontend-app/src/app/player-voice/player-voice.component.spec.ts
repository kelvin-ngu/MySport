import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlayerVoiceComponent } from './player-voice.component';

describe('PlayerVoiceComponent', () => {
  let component: PlayerVoiceComponent;
  let fixture: ComponentFixture<PlayerVoiceComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [PlayerVoiceComponent]
    });
    fixture = TestBed.createComponent(PlayerVoiceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
